# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.2.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import neblioapi
from neblioapi.api.json_rpc_api import JSONRPCApi  # noqa: E501
from neblioapi.rest import ApiException


class TestJSONRPCApi(unittest.TestCase):
    """JSONRPCApi unit test stubs"""

    def setUp(self):
        self.api = neblioapi.api.json_rpc_api.JSONRPCApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_json_rpc(self):
        """Test case for json_rpc

        Send a JSON-RPC call to a localhost neblio-Qt or nebliod node  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
