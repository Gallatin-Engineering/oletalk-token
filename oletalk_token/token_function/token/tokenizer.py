# <LEGAL WARNING & DISCLAIMER>

"""
MODULE: tokenizer
"""


import tokenizer
import time



class Token:
    """
    """

    ALLOWED_TOKEN_TYPES = ("OTT", "OTP", "OTB", "OTG")


    def __init__(self, token_type, data, *args, **kwargs):
        if token_type in ALLOWED_TOKEN_TYPES:
            self.type = token_type
        else:
            raise ValueError('Unknown token type.')
        self.token_id = self.get_token_id()
        self.header = self.create_header()
        self.body = data    

    def __str__(self):
        return 

    def __unicode__(self):
        return 

    def serialize(self):
        '''
        '''
        pass

    def load_body():
        '''
        '''
        pass 

    def get_token_id(self):
        '''
        '''
        return f"TOKEN_{time.ctime()}"

    def create_header(self):
        '''
        type, oletalk_id/anonymous_id(signature_public_key), 
        '''
        self.header = {
            'type': self.type,
            'id': self.token_id,
            'vKey': self.get_signature_verification_key()
        }

    def get_signature_verification_key():
        '''
        '''
        pass 



# module runner
def main():
    # runner
    pass

if __name__ == "__main__":
    main()