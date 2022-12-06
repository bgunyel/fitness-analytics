import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError

import os
import datetime
import json

import constants


def request_token():
    f = open(constants.GURU_ENV_FILE, 'r')
    env_data = json.load(f)
    f.close()

    client_id = env_data['client_id']
    client_secret = env_data['client_secret']

    method = 'post'
    kwargs = {'url': 'https://customer-console-prod.auth.us-west-2.amazoncognito.com/oauth2/token',
              'headers': {'content-type': 'application/x-www-form-urlencoded'},
              'data': {'grant_type': 'client_credentials',
                       'scope': 'https://api.getguru.fitness/default'},
              'auth': HTTPBasicAuth(client_id, client_secret)}

    response = requests.request(method, **kwargs)
    response_json = response.json()
    response_json['date'] = response.headers['date']

    with open(constants.GURU_TOKEN_FILE, 'w') as outfile:
        json.dump(response_json, outfile)

    return response_json['access_token']


def get_token():
    if os.path.exists(constants.GURU_TOKEN_FILE):
        f = open(constants.GURU_TOKEN_FILE)
        token_data = json.load(f)
        f.close()

        token_time = datetime.datetime.strptime(token_data['date'], '%a, %d %b %Y %H:%M:%S %Z')
        diff_seconds = (datetime.datetime.utcnow() - token_time).total_seconds()

        if diff_seconds < token_data['expires_in']:  # if the token is still alive
            access_token = token_data['access_token']
        else:
            access_token = request_token()

    else:
        access_token = request_token()

    return access_token



def get_guru():
    access_token = get_token()

    dummy = -32
