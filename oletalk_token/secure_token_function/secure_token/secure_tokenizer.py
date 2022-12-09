# <LEGAL WARNING & DISCLAIMER>

"""
MODULE: secure_token_manager
"""
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from token_function.token.token_manager import Token
import boto3



class SecureToken(Token):
    ''' '''
    ENCRYPTION_KEY=''       #  In PEM format
    DECRYPTION_KEY=''       #  In PEM format

    def __init__(self, *args, **kwargs):
       ...

    
    def encrypt_data(self, data):
        ''' '''
        rsa_public_key = RSA.importKey(self.ENCRYPTION_KEY)
        rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
        encrypted_data = rsa_public_key.encrypt(data)
        #encrypted_text = b64encode(encrypted_data)
        return encrypted_data




class OletalkSecurityKeys:
    """ """
    def __init__(self, *args, **kwargs):
        ''' '''
        ...

    

class Secure_Token_Key(models.Model):
    """  """

    def __str__(self):
        return 

    def __unicode__(self):
        return 

    def encrypt_data(self, data):
        ''' '''
        rsa_public_key = RSA.importKey(self.)
        rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
        encrypted_text = rsa_public_key.encrypt(data)
        #encrypted_text = b64encode(encrypted_text)

    def decrypt_data(self, encrypted_data):
        ''' '''
        ...


BIT_RATE=4096

def rsa_encrypt_decrypt():
    key = RSA.generate(BIT_RATE)
    private_key = key.export_key('PEM')
    public_key  = key.publickey().exportKey('PEM')


    rsa_public_key = RSA.importKey(public_key)
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(message)
    #encrypted_text = b64encode(encrypted_text)

    print('your encrypted_text is : {}'.format(encrypted_text))


    rsa_private_key = RSA.importKey(private_key)
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    decrypted_text = rsa_private_key.decrypt(encrypted_text)

    print('your decrypted_text is : {}'.format(decrypted_text))


class SecureTokenKey(RSA_Key_Wrapper):
    """RSA keys with loose association to users' identity."""

    TABLE_NAME='key_database'
    DB=boto3.resource('dynamodb')
    keydb = DB.table(TABLE_NAME)
    S3 = boto3.client('s3')

    def __init__(self, oletalkID=None):
        ''' '''
        #   get keys from key db 
        if oletalkID == None:
            self.oletalkID = self.generate_temporary_oletalkID()
            self.generate_new_key()
        else:
            self.oletalkID = oletalkID
            self.load_keys()

    def generate_temporary_oletalkID(self):
        ''' '''
        ...

    def generate_new_key_pair(self):
        '''New security(encryption) keys. \n  '''
        self.key_pair = RSA.generate(BIT_RATE)
        self.private_key = self.key_pair.export_key('PEM')
        self.public_key  = self.key_pair.publickey().exportKey('PEM')


    def load_keys(self):
        '''     '''
        keys = {
            "private": "",
            "public" : ""
        }
        for key in keys:
            filename = f"{self.oletalkID}_encryption_{key}"
            response = self.S3.download_file('KEYS', keys[key], filename)
        self.private_key = keys['private']
        self.public_key  = keys['public']

    def save_keys(self) -> None:
        '''         '''
        keys = {'public': self.private_key, 'private': self.public_key}
        for key in keys:
            filename = f"{self.oletalkID}_encryption_{key}"
            response = self.S3.upload_file('KEYS', keys[key], filename)


    def __str__(self):
        return 

    def __unicode__(self):
        return 

    def encrypt_data(self, data) -> str:
        '''data (str, req): serialized dict obj. '''
        plain_text = input(data)
        encoded_data = str.encode(plain_text)

        return encrypted_text

    def decrypt_data(self, encrypted_text) -> str:
        '''sig (str, req): Signature of serialized data obj/dict. '''
        return decrypted_text 


    # key = RSA.generate(BIT_RATE)
    # private_key = key.export_key('PEM')
    # public_key  = key.publickey().exportKey('PEM')
    # message = input('plain text for RSA encryption and decryption:')
    # message = str.encode(message)






def main():
    pass 

if __name__ == "__main__":
    main()

