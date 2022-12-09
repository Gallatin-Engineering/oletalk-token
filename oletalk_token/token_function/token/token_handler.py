# <LEGAL WARNING & DISCLAIMER>

"""
PACKAGE:    oletalk_token   (library/package)
MODULE:     token_manager
AUTHOR:     muddicode@sauceCode
VERSION:    0.02.00
CLASSES:    Token, Secured_Token, Token_Handler, Secured_Token_Handler
EXCEPTIONS: SignatureVerificationError, TokenError
"""


# from email.headerregistry import UnstructuredHeader

import time
import json
import boto3
import random
import binascii
import http_response
# from urllib import response
from Crypto.PublicKey import RSA
from botocore.exceptions import ClientError
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme

# from exceptions import TokenException, TokenSignatureError, TokenHandlingException
# import oletalk.token_manager.Token.token.token_manager as token_manager


DATABASE = boto3.resource('dynamodb')
TABLE_NAME='OLETALK_TOKEN'
KEY_TABLE='KeyDb'






#   extends the 'Token' class.
class Token_Handler:
    """Accepts OleTalk Tokens and processes them to yield their payload data.     \n
    Payload accessible as useful data.
    """


    def __init__(self, token):
        self.token = token
        head, body, sig = self.explode()
        self.header = self.deserialize(head)
        self.body = self.deserialize(body)
        #   verify signature 
        if self.verify(sig, self.header['vKey']):
            print("Token Authenticated.")
        else:
            raise TokenSignatureError("Could not verify the token's signature.")

    def explode(self):
        '''Breaks up the token into its three string components. '''
        string.split(self.token, '.')
        return (head, body, sig)

    def verify(self, signature, body, key) -> bool:
        '''Verifies the token was sent by the sender indicated.'''
        if self.token['vKey']:
            raise MissingVerificationKeyError('Token has no verification key (public key) signed.')
        KEY = self.header['vKey']
        # RSA_functions_verify_signature(signature, data, KEY)
        # TokenSignatureError


    def parse_token(self):
        '''Separate the Token parts into head, body & signature. '''
        self.header = self.parse_token
        self.body = self.token 
        self.signature  = self.token 
        # TokenFormatError

    def deserialize(self, component):
        ''' Turns a serialized component (header or body) of the token, into python dict. '''
        data = json.loads(component)
        return data

    def extract_data(self, data_key):
        '''Returns the value for a given key in the token. '''
        if self.header[data_key]:
            return self.header[data_key]
        elif self.body[data_key]:
            return self.body[data_key]
        else:
            raise TokenKeyError('Token does not contain the requested DATA.')
    
    # def deconstruct(self, oletalk_token):
    #     '''
    #     Split up the string that represents the token, into its logical parts.
    #     '''
    #     header = oletalk_token          #   split('.')
    #     body = oletalk_token
    #     signature = oletalk_token
    #     return header, body, signature   

    # def verify_sender_signature(self):
    #     '''
    #     '''
    #     key = self.header['vKey'] 

