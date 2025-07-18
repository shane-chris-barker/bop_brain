import unittest
from requests.exceptions import RequestException
from unittest.mock import Mock, patch
from ip.client.ipify_ip_client import IpifyIpClient

class TestIpifyIpClient(unittest.TestCase):

    @patch("requests.get")
    def test_get_public_ip_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"ip": "123.123.123.123"}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        client = IpifyIpClient()
        result = client.get_public_ip()

        self.assertEqual(result, "123.123.123.123")
        mock_get.assert_called_once_with("https://api.ipify.org?format=json")

    @patch("requests.get", side_effect=RequestException("Network Error"))
    def test_public_ip_request_exception(self, mock_get):
        client = IpifyIpClient()
        result = client.get_public_ip()
        self.assertIsNone(result)
        mock_get.assert_called_once()
