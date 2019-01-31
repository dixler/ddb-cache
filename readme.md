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
# "Your scientists were so preoccupied with whether or not they could, they didn’t stop to think if they should."
#   -Jurassic Park

while k['counter']['data'] < 100:
    val = k['counter']
    print('counter:', val)
    val['data'] += 1
    k['counter'] = val

```
