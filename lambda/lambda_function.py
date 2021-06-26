import boto3
import json
import logging
import time
import uuid

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DYNAMO_TABLE = 'PiDoorBellV2'

APPLIANCES = [
    {
        'applianceId': 'endpoint-001',
        'manufacturerName': 'Br0t Labs',
        'modelName': 'PIDoorBell',
        'version': '2',
        'friendlyName': 'piDoorbellv2',
        'friendlyDescription': '001 Lock that can be locked and can query lock state',
        'isReachable': True,
        'actions': [
            'setLockState',
            'getLockState'
        ],
        'additionalApplianceDetails': {}
    }
]

def default_response():
    '''
    Placeholder function in case it's needed later.
    '''

    return {}


def discovery():
    '''
    Return our mock IoT doorbell for discovery.
    '''

    return {
        'event': {
            'header': {
                'namespace': 'Alexa.Discovery',
                'name': 'Discover.Response',
                'payloadVersion': '3',
                'messageId': str(uuid.uuid4())
            },
            'payload': {
                'endpoints': [
                    {
                        'endpointId': 'endpoint-001',
                        'manufacturerName': 'Br0t Labs',
                        'friendlyName': 'PIDoorBell',
                        'description': 'Lock that can be locked and can query lock state',
                        'displayCategories': ['DOORBELL'],
                        'cookie': {},
                        'capabilities': [
                            {
                                'type': 'AlexaInterface',
                                'interface': 'Alexa.DoorbellEventSource',
                                'version': '3',
                                'proactivelyReported' : True
                            }
                        ]
                    }
                ]
            }
        }
    }


def lambda_handler(event, context):
    '''
    '''

    client = boto3.client('dynamodb')

    print('Event:')
    print(json.dumps(event, indent=4, sort_keys=True, default=str))

    print('Context:')
    print(json.dumps(event, indent=4, sort_keys=True, default=str))

    result = None

    if event['directive']['header']['name'] == 'Discover':
        result = discovery()
    elif event['directive']['header']['namespace'] == 'Alexa.Authorization':
        if event['directive']['header']['name'] == 'AcceptGrant':
            result = {
                'event': {
                    'header': {
                        'namespace': 'Alexa.Authorization',
                        'name': 'AcceptGrant.Response',
                        'payloadVersion': '3',
                        'messageId': str(uuid.uuid4())
                    },
                    'payload': {}
                }
            }
        # Store access code
        client.put_item(
            TableName=DYNAMO_TABLE,
            Item={
                'user': { 'S': event['directive']['payload']['grantee']['token'] },
                'access_code': { 'S': event['directive']['payload']['grant']['code'] },
                'last_refreshed': { 'S': '0' },
                'refresh_token': { 'S': '' }
            }
        )
    else:
        result = default_response()

    print('Response:')
    print(json.dumps(result, indent=4, sort_keys=True, default=str))

    return result
