import unittest
from unittest import mock

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
            self.decode_content = True
            self.response_data = response_data
            self.status_code = status_code
            self.raw = RawData(self.response_data)

    if args[0] == 'http://existing_device.local/sc2_val.xml':
        res = MockResponse(strValidResponseData, 200)

        return res

    return MockResponse(None, 404)

def mocked_elementtree_parse(*args, **kwargs):

    class MockData:
        def __init__(self):
            self.text = "AA5555AA056B12381B060012007602EB012101B701DB00DC00A2FE92003701900087013D016701C409C409C40900000000000000000000004C4C0D00000000000000006464006400000000000000005536C12CC705CC3580CF0100010104000000020202010096CC000000170317639900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

    class MockElement:
        def __init__(self):
            self.mock_data = MockData()

        def find(self, tag:str):
            return self.mock_data
        
    class MockParse:
        def __init__(self):
            self.mock_data = MockElement()


        def getroot(self):
            return self.mock_data

    return MockParse()

class TestValidator(unittest.TestCase):
    def test_query_host_negative(self):
        """Test host validator with a not existing host"""

        testPassed = False
        try:
            o = SC2XMLReader("http://not_existing_host.local", DEFAULT_USERNAME, DEFAULT_PASSWORD)
        except:
            testPassed = True

        self.assertFalse(testPassed)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('defusedxml.ElementTree.parse', side_effect=mocked_elementtree_parse)
    def test_parse_positive(self, mock_get, mock_parse):
        """Basictest for data processing"""        
        o = SC2XMLReader("http://existing_device.local", DEFAULT_USERNAME, DEFAULT_PASSWORD)

        self.assertEqual(o.data["temperature_buffer_top"]["Value"], 63.0)
        self.assertEqual(o.get_value("temperature_buffer_top"), 63.0)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('defusedxml.ElementTree.parse', side_effect=mocked_elementtree_parse)
    def test_check_data_elements(self, mock_get, mock_parse):
        """Test is all supported data element are in the dictionary"""        
        o = SC2XMLReader("http://existing_device.local", DEFAULT_USERNAME, DEFAULT_PASSWORD)

        for value in o.MAP_SOLVIS_TO_NAME.values():
            self.assertIsNotNone(o.data[value])

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('defusedxml.ElementTree.parse', side_effect=mocked_elementtree_parse)
    def test_get_value(self, mock_get, mock_parse):
        """Test is all supported data element are in the dictionary with get_value method"""
        o = SC2XMLReader("http://existing_device.local", DEFAULT_USERNAME, DEFAULT_PASSWORD)

        for value in o.MAP_SOLVIS_TO_NAME.values():
            self.assertIsNotNone(o.get_value(value))

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('defusedxml.ElementTree.parse', side_effect=mocked_elementtree_parse)
    def test_get_data(self, mock_get, mock_parse):
        """Test is all supported data element are in the dictionary with get_data method"""
        o = SC2XMLReader("http://existing_device.local", DEFAULT_USERNAME, DEFAULT_PASSWORD)

        for value in o.MAP_SOLVIS_TO_NAME.values():
            self.assertIsNotNone(o.get_data(value))

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('defusedxml.ElementTree.parse', side_effect=mocked_elementtree_parse)
    def test_get_value_without_warm_water_station(self, mock_get, mock_parse):
        """Test if values for warmwater station are left out, when disabled"""
        o = SC2XMLReader("http://existing_device.local", username=DEFAULT_USERNAME, password=DEFAULT_PASSWORD, withWarmWaterStation=False)

        self.assertEqual(o.get_value("temperature_buffer_top"), 63.0)
        self.assertIsNone(o.get_value("volume_stream_warm_water"))

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('defusedxml.ElementTree.parse', side_effect=mocked_elementtree_parse)
    def test_get_value_no_warm_water_nor_solar(self, mock_get, mock_parse):
        """Test if values for warmwater station and solar are left out, when disabled"""
        o = SC2XMLReader("http://existing_device.local", username=DEFAULT_USERNAME, password=DEFAULT_PASSWORD, withWarmWaterStation=False, withSolar=False)

        self.assertEqual(o.get_value("temperature_buffer_top"), 63.0)
        self.assertIsNone(o.get_value("volume_stream_warm_water"))
        self.assertIsNone(o.get_value("temperature_solar_panel"))
