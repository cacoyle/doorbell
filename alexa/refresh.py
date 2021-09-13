#!env/bin/python

mport boto3
import config
import json
import requests
import uuid

client = boto3.client(
        'dynamodb',
        region_name=config.REGION,
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
)

users = client.scan(TableName=config.USER_TABLE)

breakpoint()

# Initial Token
token = requests.post(
    'https://api.amazon.com/auth/o2/token',
    headers={
        # 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        'Content-Type': 'application/json'
    },
    json={
        # 'grant_type': 'authorization_code',
        'grant_type': 'refresh_token',
        # 'code': users['Items'][0]['access_code']['S'],
        'refresh_token': users['Items'][0]['refresh_token']['S'],
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET
    }
)

breakpoint()

with open('token_debug.log', 'a') as logfile:
    logfile.write(json.dumps(token.json(), indent=4, sort_keys=True, default=str))

