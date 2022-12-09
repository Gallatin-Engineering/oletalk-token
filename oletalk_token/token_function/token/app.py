# <LEGAL WARNING & DISCLAIMER>

import json
from token_handler import Token_Handler
from token_manager import Token


"""
MODULE: app (AWS Lambda module)
"""


def lambda_function(event, context):
    ''' '''
    if event['httpMethod'] == 'POST':
        data = json.loads(event['body'])
        return tokenize(data)
    
    if event['httpMethod'] == 'POST':
        return handle_token(event['queryStringParameters'])

    return "Token protocol not recognized."


def tokenize(data):
    ''' '''    
    lambda_token = Token(data)
    return lambda_token


def handle_token(token):
    ''' '''
    data = Token_Handler(token)
    return data 
