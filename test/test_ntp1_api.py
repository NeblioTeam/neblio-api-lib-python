# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.2.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import neblioapi
from neblioapi.api.ntp1_api import NTP1Api  # noqa: E501
from neblioapi.rest import ApiException


class TestNTP1Api(unittest.TestCase):
    """NTP1Api unit test stubs"""

    def setUp(self):
        self.api = neblioapi.api.ntp1_api.NTP1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_broadcast_tx(self):
        """Test case for broadcast_tx

        Broadcasts a signed raw transaction to the network  # noqa: E501
        """
        pass

    def test_burn_token(self):
        """Test case for burn_token

        Builds a transaction that burns an NTP1 Token  # noqa: E501
        """
        pass

    def test_get_address_info(self):
        """Test case for get_address_info

        Information On a Neblio Address  # noqa: E501
        """
        pass

    def test_get_token_holders(self):
        """Test case for get_token_holders

        Get Addresses Holding a Token  # noqa: E501
        """
        pass

    def test_get_token_id(self):
        """Test case for get_token_id

        Returns the tokenId representing a token  # noqa: E501
        """
        pass

    def test_get_token_metadata_of_issuance(self):
        """Test case for get_token_metadata_of_issuance

        Get Issuance Metadata of Token  # noqa: E501
        """
        pass

    def test_get_token_metadata_of_utxo(self):
        """Test case for get_token_metadata_of_utxo

        Get UTXO Metadata of Token  # noqa: E501
        """
        pass

    def test_get_transaction_info(self):
        """Test case for get_transaction_info

        Information On an NTP1 Transaction  # noqa: E501
        """
        pass

    def test_issue_token(self):
        """Test case for issue_token

        Builds a transaction that issues a new NTP1 Token  # noqa: E501
        """
        pass

    def test_send_token(self):
        """Test case for send_token

        Builds a transaction that sends an NTP1 Token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()