# Summary

This basically lets you access DynamoDB as if it were a native dictionary

``` python3
#!/usr/bin/env python3

import boto3
from ddbcache import DDBCache

k = DDBCache('dev-dev-table') # use your specific DynamoDB table name

k['counter'] = {'data': 0}
print(k['counter'])

# example: a for loop in the cloud

while k['counter']['data'] < 100:
    val = k['counter']
    print('counter:', val)
    val['data'] += 1
    k['counter'] = val

```
