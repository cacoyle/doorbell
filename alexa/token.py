#!env/bin/python

import boto3
import requests
import uuid

class AlexaEventToken(object):
    '''
    Class for managing Alexa Event tokens.
    '''

    __TOKEN_ENDPOINT = 'https://api.amazon.com/auth/o2/token'

    def __init__(config, user):
        '''
        Class initialization.
        '''

        self.dynamo = boto3.client(
            'dynamodb',
            region_name=config.REGION,
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
        )

        self.users = self.dynamo.scan(TableName=config.USER_TABLE)

    def initial_token(self, config, user):
        '''
        Get an initial auth token from the token service.
        '''

        result = requests.post(
            self.__TOKEN_ENDPOINT,
            headers={
                'Content-Type': 'application/json'
            },
            json={
                'grant_type': 'authorization_code',
                'code': user['code'], # TODO
                'client_id': config.CLIENT_ID,
                'client_secret': config.CLIENT_SECRET
            }
        )

        return result

    def refresh_token(self, config, user):
        '''
        Refresh an authorization token.
        '''

        pass # TODO
