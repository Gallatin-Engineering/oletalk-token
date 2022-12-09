#



#

TOKEN_TYPES = ("OTT", "OTP", "OTB", "OTG", "OTO")    #  each type has a unique data schema in the body of a token.

class TokenTypeError(Exception):
    ''' '''
    ...


def get_token_data_schema(token_type):      # 
    ''' returns the schema for the given type of Token  '''
    #   oletalk communications token
    SCHEMA = {
        'OTT': {
            "server": "",   # chat server (partition key)
            "id": "",       # message ID (sort key)
            "type": "message",  # message, user/connection, room
            "oletalkID": "",
            "alias": "",
            "user": "",
            "datetime": "",
            "room": "", 
            "message_text": ""
        },
    #   oletalk crypto currency payment token
        'OTP': {
            "id": "",   # token ID
            "type": 'OTP',     #   transaction ID
            "oletalkID": "",
            "userid": "",
            "alias": "",
            "payee": "",
            "payment": "500",
            "current_balance": "",
            "prior_balance": "", 
            "transaction_status": ""
        },
        'OTG': {},       
        'OTO': {}       #   OPEN OR BLANK WILDCARD SCHEMA
    }
    return SCHEMA[token_type]
