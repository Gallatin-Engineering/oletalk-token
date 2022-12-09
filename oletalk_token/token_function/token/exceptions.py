





class TokenException(Exception):
    """ Token Class Error Handling  """
    
    def __init__(self, *args, **kwargs):
        ...


class TokenSignatureError(TokenException):
    ''' ''' 
    ...


class TokenProcessingError(TokenException):
    """ Token Handling Exceptions   """
    ...
