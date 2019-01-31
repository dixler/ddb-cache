'''
This library allows dictionary-esque access to DynamoDB tables

it shouldn't be so hard to just get data from a database so
this library should simplify it much more.
'''

import boto3
from boto3.dynamodb.conditions import Key, Attr


class DDBCache:
    dynamodb = boto3.resource('dynamodb')

    def __init__(self, TableName, RangeKey=None):
        "initialize the table using the table's name"
        self.table = self.dynamodb.Table(TableName)
        key_schema = self.table.key_schema
        self.PrimaryKey = key_schema[0]['AttributeName']
        self.RangeKey = None
        if len(key_schema) > 1:
            self.RangeKey = key_schema[1]['AttributeName']
            if RangeKey == None:
                raise Exception('missing range key')
            self.RangeKeyValue = RangeKey


    def __getitem__(self, key):
        'allow bracket access on primary key, returns a dictionary'
        try:
            Key = {self.PrimaryKey: key}

            if self.RangeKey != None:
                Key[self.RangeKey] = self.RangeKeyValue

            return self.table.get_item(Key=Key)['Item']
        except Exception:
            return None

    def __setitem__(self, key, value):
        'allow bracket modification on primary key, must store as a dictionary'
        if not isinstance(value, dict):
            raise Exception('value is not of type dict')
        item = {**value, **{self.PrimaryKey: key}}
        return self.table.put_item(Item=item)

    def __delitem__(self, key):
        return self.table.delete_item(Key={self.PrimaryKey: key})

