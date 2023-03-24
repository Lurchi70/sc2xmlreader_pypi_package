import unittest
from unittest import mock

from sc2xmlreader.sc2xmlreader_validator import SC2XMLReaderValidator

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://existing_device.local':
        return MockResponse({"key1": "value1"}, 200)
    elif args[0] == 'http://existing_user.local':
        return MockResponse({"key1": "value1"}, 200)
    elif args[0] == 'http://invalid_user.local':
        return MockResponse({"key1": "value1"}, 401)
    elif args[0] == 'http://someotherurl.com/anothertest.json':
        return MockResponse({"key2": "value2"}, 200)

    return MockResponse(None, 404)

class TestValidator(unittest.TestCase):
    def test_validate_host_negative(self):
        """Test host validator with a not existing host"""
        o = SC2XMLReaderValidator("not_existing_host.local")

        self.assertFalse(o.validate_host())

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_validate_host_positive(self, mock_get):
        """Test host validator with a not existing host"""        
        o = SC2XMLReaderValidator("existing_device.local")

        self.assertTrue(o.validate_host())

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_authenticate_positive(self, mock_get):
        """Test host validator with a valid user"""        
        o = SC2XMLReaderValidator("existing_user.local")

        self.assertTrue(o.authenticate("peter", "peters_password"))

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_authenticate_negative(self, mock_get):
        """Test host validator with a invalid user"""        
        o = SC2XMLReaderValidator("invalid_user.local")

        self.assertFalse(o.authenticate("peter", "peters_password"))
