import unittest
from unittest.mock import patch, MagicMock
from location.client.ip_geo_location_client import IPGeoLocationClient
from location.dtos.location_dto import LocationDTO
from ip.client.get_ip_client_interface import IPClientInterface
import requests

class TestIPGeoLocationClient(unittest.TestCase):
    def setUp(self):
        self.mock_ip_client = MagicMock(spec=IPClientInterface)
        self.mock_ip_client.ip = "123.123.123.123"
        self.api_key = "MOCK_API_KEY"
        self.client = IPGeoLocationClient(
            api_key=self.api_key,
            ip_client=self.mock_ip_client
        )

    def test_ready_returns_true_when_api_key_and_ip_is_present(self):
        self.assertTrue(self.client.ready())
        self.mock_ip_client.get_public_ip.assert_called_once()

    @patch.dict("os.environ", {}, clear=True)
    def test_ready_returns_false_when_no_api_key(self):
        client = IPGeoLocationClient(api_key=None, ip_client=self.mock_ip_client)
        client._ip = "8.8.8.8"
        self.assertFalse(client.ready())

    def test_ready_returns_false_when_ip_resolution_fails(self):
        self.mock_ip_client.get_public_ip.side_effect = requests.RequestException("Network Error")
        client = IPGeoLocationClient(api_key=self.api_key, ip_client=self.mock_ip_client)
        self.assertFalse(client.ready())

    @patch("location.client.ip_geo_location_client.requests.get")
    def test_get_location_successful(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "location": {
                "city": "Test City",
                "country_name": "United Kingdom",
                "latitude": "52.9548",
                "longitude": "-1.1581",
                "continent_name": "Europe",
                "zipcode": "TE5 1NN",
                "district": "Test District",
            }
        }

        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        self.client._ip = "8.8.8.8"
        location = self.client.get_location()
        self.assertIsInstance(location, LocationDTO)
        self.assertEqual(location.city, "Test City")
        self.assertEqual(location.country, "United Kingdom")
        self.assertEqual(location.latitude, 52.9548)
        self.assertEqual(location.longitude, -1.1581)
        self.assertEqual(location.zipcode, "TE5 1NN")
        self.assertEqual(location.district, "Test District")
        self.assertEqual(location.continent, "Europe")
        mock_get.assert_called_once()
        self.assertIn("8.8.8.8", mock_get.call_args[0][0])
