#!env/bin/python

import requests
import time
import uuid
import json

import pdb

import logging
import sys
import os

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def get_utc_timestamp(seconds=None):
    return time.strftime("%Y-%m-%dT%H:%M:%S.00Z", time.gmtime(seconds))

def get_uuid():
    return str(uuid.uuid4())

event_endpoint = "https://api.amazonalexa.com/v3/events"
token_endpoint = "https://api.amazon.com/auth/o2/token"

auth_token = 'hotyb'

payload = {
    "context": { },
    "event": {
        "header": {
            "messageId": get_uuid(),
            "namespace" : "Alexa.DoorbellEventSource",
            "name": "DoorbellPress",
            "payloadVersion": "3"
        },
        "endpoint": {
            "scope": {
                "type": "BearerToken",
                "token": auth_token
            },
            "endpointId": "endpoint-001"
        },
        "payload" : {
            "cause": {
                "type": "PHYSICAL_INTERACTION"
            },
            "timestamp": get_utc_timestamp()
        }
    }
}

result = requests.post(
        event_endpoint,
        headers={
            "Authorization": "Bearer %s" % auth_token,
            "Content-Type": "application/json"
        },
        json=payload
)

pdb.set_trace()

print(result.status_code)
