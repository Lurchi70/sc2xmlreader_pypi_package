import unittest
from unittest import mock
from requests import Response

from sc2xmlreader.sc2xmlreader import SC2XMLReader
from sc2xmlreader.const import DEFAULT_USERNAME, DEFAULT_PASSWORD

strValidResponseData = """<xml>
<data>
AA5555AA056B12381B060012007602EB012101B701DB00DC00A2FE92003701900087013D016701C409C409C40900000000000000000000004C4C0D00000000000000006464006400000000000000005536C12CC705CC3580CF0100010104000000020202010096CC000000170317639900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
</data>
</xml>"""

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class RawData:
        def __init__(self, raw_data):
            self.raw_data = raw_data
            self.decode_content = True

        def __str__(self):
            return self.raw_data

    class MockResponse:
        def __init__(self, response_data, status_code):
            self.response_data = response_data
            self.status_code = status_code

        def raw(self):
            return RawData(self.response_data)

    if args[0] == 'http://existing_device.local/sc2_val.xml':
        res = Response()
        res.raw = strValidResponseData
        res.status_code = 200

        return res

    return MockResponse(None, 404)

class TestValidator(unittest.TestCase):
    def test_query_host_negative(self):
        """Test host validator with a not existing host"""

        #testPassed = False
        #try:
        #    o = SC2XMLReader("http://not_existing_host.local", DEFAULT_USERNAME, DEFAULT_PASSWORD)
        #except:
        #    testPassed = True

        #self.assertFalse(testPassed)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_validate_host_positive(self, mock_get):
        """Test host validator with a not existing host"""        
        #o = SC2XMLReader("http://existing_device.local", DEFAULT_USERNAME, DEFAULT_PASSWORD)

        #self.assertEqual(o.data["S0"], 65.0)
