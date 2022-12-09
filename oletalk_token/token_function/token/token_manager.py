# * Copyright (c) 2022 Gallating Engineering Ltd. All rights reserved.
# * @License: MIT
# * SP: Commercial

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
from token_schema import TOKEN_TYPES
from urllib import response
from Crypto.PublicKey import RSA
from botocore.exceptions import ClientError
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme

# from exceptions import TokenException, TokenSignatureError, TokenHandlingException
# import oletalk.token_manager.Token.token.token_manager as token_manager


DATABASE = boto3.resource('dynamodb')
TABLE_NAME='OLETALK_TOKEN'
KEY_TABLE='KeyDb'



class Token:
    """Unsecured Token class
    HEADER: token id, type, vkey (verification key in PEM format), destination id, sender's id or contact
    BODY:   stringified DATA
    SIG:    signature of body
    """
#   'OTT'   ->  'OleTalk Token' (for chat),       'OTP'   ->  'OleTalk Pay'      'OTO'   ->  'OleTalk Open' (for any data schema)
#   'OTB'   ->  'OleTalk Betting',                'OTG'   ->  'OleTalk Gaming'
    # TOKEN_TYPES = ("OTT", "OTP", "OTB", "OTG", "OTO")
    SIGNING_KEY=''                      #   Private Key in PEM format
    VERIFICATION_KEY=''                 #   Public Key  in PEM format


    def __init__(self, token_type, userid, dest, data=None) -> None:
        '''Generates a new token from the given data.     \n

        Parameters:
        -----------
            token_type (str, req):
                Determines the specific type and use of the token.  \n 

            data (dict, opt): 
                The key-value pairs of information that will form the token.      \n

            userid (str, opt.):
                Contact or some other unique identifier of the token's creator.     \n
            
            otid (str, req.):
                Sender's unique identifier.

            dest (str, opt.):
                Destination identifier.     \n
        
        Returns:
        --------
            return: 
                None.
        
        '''
        if token_type not in self.ALLOWED_TOKEN_TYPES:
            print('UnsupportedTokenTypeError: use OT Open format instead.')
            # raise UnsupportedTokenTypeError('Unsupported token. Use the Open Token Format type instead.')       # Unsupported Token Error
        self.token_type = token_type
        if data == None:
            print('EmptyTokenError: Token body has no data. Aborting...')
            # raise EmptyTokenDataError('Token has no data. Aborting...')
        self.data = data
        self.header = self.serialize(self.create_header())
        # self.body = self.serialize(self.data)
        # self.signature = self.sign(self.SIGNING_KEY)
    
    def __str__(self):
        return self.export()

    def __unicode__(self):
        return 

    @classmethod
    def __hasattr(cls, object, name):
        return name in object.__class__.__dict__

    def create_header(self) -> None:
        '''Creates standard token header.  '''
        self.token_id = self.get_token_id()
        return {
            'id'  : self.token_id,    # GENERATE TOKEN ID
            'type': self.token_type,
            'vkey': self.VERIFICATION_KEY, 
            'contact': '',      # optional - sender's contact etc
            'userid': "[oletalkID/uniqueUserId]", 
            'otid': '', 
            'dest': "[DESTINATION ID]"  # Could be left blank or use generic terms such as 'SERVER' in some cases.
        }
  
    def serialize(self, obj_data) -> str:
        ''' Makes a json object (represented as a string) from the provided data. '''
        return json.dumps(obj_data)

# ****@DEBUG****
    def sign(self, KEY) -> object:
        '''Cryptographic hash of the serialized data in the body of the token.     \n
        Parameters:
        -----------
            KEY (str, req):
                The private key in PEM format.
        
        Returns:
        --------
            return (str, req):
                The cryptographic signature of the body of the token.  \n

        '''
        #   get cryptographic keys: new or existing
        #   KEY['sign']['private']
        self.signature = sign(KEY)
        return self 

    def export(self) -> str:
        ''' Returns Token as a single string. Also, enters token into database.'''
        self.body = self.serialize(self.data)
        self.signature = self.sign(self.SIGNING_KEY)
        self.id = self.generate_token_id()
        token=self.get_token_db_key()
        response = self.upload_token(token)
        if response[''] == 200:
            return f"{self.header}.{self.body}.{self.signature}"
        else:
            ...
            # throw exception: Token Database Error --> "Cannot generate token. Abort."


    def generate_token_id(self) -> str:
        '''Generate a unique id for the token itself.'''
        return f"{self.type}_{time.ctime()}"
    
    def get_token_db_key(self):
        ''' Returns a unique dynamoDB key for the token. '''
        n = random.randint(10, 15)      #  random.randint(10, 99) 
        partition_key = f"{self.type}_{n}"
        sort_key = f"{self.token_id}"
        return {
            "type": partition_key,
            "id": sort_key          #   token id not user id 
        }

    def upload_token(self, database_key) -> dict:
        ''' Store token in dynamoDB database table. '''
        data = database_key
        data.update(self.export())
        tokenDB = DATABASE.table(TABLE_NAME)
        try:
            db_response = tokenDB.put_item(Item=data)
        except ClientError as cerr:
            data = cerr.response['Error']
            code=cerr.response['Error']['Code']
            message=cerr.response['Error']['Message']
            print(f"{code}: {message}. -->  {data}")
        except Exception as e:
            code=400
            message = "ERROR: An exception occurred. Check logs for details."
            data = e
            print(f"{code}: {message}. -->  {data}")
        else:
            return db_response     

    def download_token(self, database_key) -> dict:
        ''' Retrieves token in dynamoDB database table. ''' 
        tokenDB = DATABASE.table(TABLE_NAME)
        try:
            db_response = tokenDB.get_item(Key=database_key)
        except ClientError as cerr:
            print(cerr.response['Error']['Code'])
            print(cerr.response['Error']['Message'])
        else:
            return db_response['Item']

    def remove_dbase_token(self, database_key):
        ''' Delete token in dynamoDB database table. ''' 
        tokenDB = DATABASE.table(TABLE_NAME)
        try:
            db_response = tokenDB.delete_item(Key=database_key)
        except ClientError as cerr:
            print(cerr.response['Error']['Code'])
            print(cerr.response['Error']['Message'])
        else:
            return db_response

    # def check_format_compliance(token_format, data) -> bool:
    #     '''Determine if data keys are consistent with the attributes of the specified format.  \n '''
    #     return True

    # def validate_token_data(self, type, data):
    #     '''        '''  
    #     ... 





   






#   ****** RSA Signature Key Functions ******


    def generate_oletalk_identity_keys():   #   public_key => id_key(verification_key) & private_key => signing_key
        ...

    def get_signature_verification_keys():
        '''
        '''
        return oletalkID

    def generate_RSA_signature_key_pair():
        '''
        Signature Key Type is the only cryptographic key type used with regular (unsecured) tokens.     \n
        '''
        KEY={}
        KEY['public']  = ""
        KEY['private'] = ""
        return KEY

    def export_keys(self, keys, key_format='PEM'):
        '''
        Converts the public key to text/string and saves it as the OleTalk ID in the users database.    \n
        '''
        if key_format == 'PEM':
            ...

    def import_keys(self, keys, key_type, key_format='PEM'):
        '''        '''
        if key_format != 'PEM':
            return "Unsupported format."

    def store_id_keys(self, location):
        '''        '''
        if location == 'local':                     #   on device
            ...
        if location == 'online storage':            #   AWS S3
            ...
        if location == 'online database':           #   AWS DynamoDB
            ...

    def retrieve_id_keys(self, location):
        '''        '''
        if location == 'local':
            ...
        if location == 'online storage':
            ...
        if location == 'online database':
            ...



class RSA_Key_Wrapper:
    ''' 
    '''
    # Higher bit rates should be used.
    _bit_rate=1024          #   For identity, etc. use 2048 for financial transactions, use 4096 bit rate
    key_db = DATABASE.Table(KEY_TABLE)

    def __init__(self, key_type):       #   signing key type or encryption key type
        self.signing_keyPair = self.generate_new_keys()
        # self.publicKey = self.signing_keyPair.publickey()

    @property
    def bit_rate(self):
        return self._bit_rate

    @bit_rate.setter
    def bit_rate(self, bit_rate):
        self._bit_rate = bit_rate 


    def generate_new_keys(self):
        ''' '''
        return RSA.generate(bits=self._BIT_RATE)


    def download_keys(self, key_location):
        try:
            resp = self.key_db.get_item(key={})
            code=200
            msg='Keys downloaded. See data.'
            data=resp['Item']
        except ClientError as cerr:
            code=cerr.response['Error']['Code']
            msg=cerr.response['Error']['Message']
            data=cerr.response['Error']['']
        except Exception as err:
            code=400
            msg='Unexpected error occurred while trying to download keys.'
            data=err.stack
        else:
            http_response(code, msg, data)

    def upload_keys(self, key_location):
        try:
            resp = self.key_db.put_item(key={})
            code=200
            msg='Keys uploaded.'
            data=resp['Item']
        except ClientError as cerr:
            code=cerr.response['Error']['Code']
            msg=cerr.response['Error']['Message']
            data=cerr.response['Error']['']
        except Exception as err:
            code=400
            msg='Unexpected error occurred while trying to download keys.'
            data=err.stack        
        else:
            http_response(code, msg, data)

    def export_keys(self):
        '''Converts keys TO ASCII text PEM format FROM BINARY.'''
        ...

    def import_keys(self):
        '''Converts keys FROM ASCII text PEM format to BINARY.'''
        ...


class Token_Key(RSA_Key_Wrapper):
    """RSA keys with loose association to users' identity."""
    def __init__(self, *args, **kwargs):
        ''' '''
        key_pair = RSA_Key_Wrapper(otid='anonymous')
        key_pair._bit_rate(2048)    #   key_pair._bit_rate(4096) for encryption keys
        self.verification_key = key_pair.public_key()
        self.identity_key = key_pair.private_key()

    def __str__(self):
        return 

    def __unicode__(self):
        return 

    def sign_data(self, data) -> str:
        '''data (str, req): serialized dict obj. '''
        return sig

    def verify_signature(self, sig) -> bool:
        '''sig (str, req): Signature of serialized data obj/dict. '''
        return False 



# module runner
def main():
    ...

if __name__ == "__main__":
    main()

#             token (str, opt): 
                # The actual token in its portable form, ie: a long single string punctuated by periods ('.')      \n 

### oletalk identification table
#   "tokenID":
#   "previousTokenID":  Token chain value that aids the recipient to recreate the intended sequence of the Token chain
#   "id": oletalkID_
#   "vKey": verification_key_in_PEM_format
#   "contact": email_OR_mobile_number
#   "origin":  
#   "destination": 
#   "verification":
#   once the signature is verified for that oletalkID create the desired token.
#

