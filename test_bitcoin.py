import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

class TestBitcoin(TestCase):

    @patch('requests.get')
    def test_bitcoin_to_dollars(self, mock_requests_get):
        mock_rate = 110022.00
        example_api_response = {"bpi": {"USD": {"code": "USD", "symbol": "&#36;","rate": "11,929.6521", "description": "United States Dollar", "rate_float": mock_rate}}}
        mock_requests_get().json.return_value = example_api_response
        rate = bitcoin.api_call()
        converted = bitcoin.convert_to_bitcoin(4, rate)
        expected = 440088.00
        self.assertEqual(expected, converted)

if __name__ == '__main__':
    unittest.main()