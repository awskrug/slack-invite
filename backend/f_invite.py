# coding: utf-8
from __future__ import print_function
from botocore.vendored import requests
import json
import boto3
from base64 import b64decode

ENCRYPTED_TOKEN = '--ENCRYPTED-TOKEN-HERE--' # noqa
kms = boto3.client('kms')
token = kms.decrypt(CiphertextBlob=b64decode(ENCRYPTED_TOKEN))['Plaintext']


def lambda_handler(event, context):
    payload = event['body-json']
    data = {
        'token': token,
        'email': payload['email'],
        'set_active': True
    }

    r = requests.post(
        'https://slack.com/api/users.admin.invite',
        data=data
    ).json()
    if not r['ok']:
        return {'result': False, 'error': r['error']}

    return {'result': True}
