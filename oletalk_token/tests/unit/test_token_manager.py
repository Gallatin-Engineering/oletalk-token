

"""
"""



from token_function.token.token_manager import Token
import unittest






class Test_Token(unittest.TestCase):
    """ """
    def setUpClass(cls) -> None:
        return super().setUp()

    def tearDownClass(cls) -> None:
        return super().tearDown()

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

#       *** Tests ***

    def test_load_token():
        ...

    def test_create_token():
        ...

    def deserialize_token():
        ...

    def test_deconstruct_token():
        ...

    def test_verify_sender_signature():
        ...

    def test_check_format_compliance():
        ...

    def test_validate_token_data():
        ...

    def test_serialize():
        ...

    def test_sign_token():
        ...

    def test_generate_token():
        ...


#   ****** Testing RSA Signature Key Functions ******

class Test_RSA_Key_Functions(unittest.TestCase):
    """ """

    def setUpClass(cls) -> None:
        print('Setting up testing environment')

    def tearDownClass(cls) -> None:
        print('Garbage collection: Removing all class data from memory.')
        return super().tearDown()

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_generate_oletalk_identity_keys():
        ...

    def test_store_id_key():
        ...

    def test_retrieve_id_key():
        ...

    def test_import_id_keys():
        ...

    def test_export_id_keys():
        ...

    def test_Security_Keys():
        ...
        

    def test_load_token_schema():
        ... 




class Test_RSA_Security_Key_Wrapper(unittest.TestCase):
    ''' '''
    
    def test_generate_new_keys(self):
        ''' '''
        ...


    def test_download_keys(self, key_location):
        ...
    
    def test_upload_keys(self, key_location):
        ''' '''
        ...

    def test_export_keys(self):
        '''Converts keys into ASCII text PEM format.'''
        ...

    def test_import_keys(self):
        '''Converts keys from ASCII text PEM format.'''
        ...
