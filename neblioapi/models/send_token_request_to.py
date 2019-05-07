# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.2.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SendTokenRequestTo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'address': 'str',
        'amount': 'float',
        'token_id': 'str'
    }

    attribute_map = {
        'address': 'address',
        'amount': 'amount',
        'token_id': 'tokenId'
    }

    def __init__(self, address=None, amount=None, token_id=None):  # noqa: E501
        """SendTokenRequestTo - a model defined in OpenAPI"""  # noqa: E501

        self._address = None
        self._amount = None
        self._token_id = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if amount is not None:
            self.amount = amount
        if token_id is not None:
            self.token_id = token_id

    @property
    def address(self):
        """Gets the address of this SendTokenRequestTo.  # noqa: E501

        Address to transfer tokens to  # noqa: E501

        :return: The address of this SendTokenRequestTo.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SendTokenRequestTo.

        Address to transfer tokens to  # noqa: E501

        :param address: The address of this SendTokenRequestTo.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def amount(self):
        """Gets the amount of this SendTokenRequestTo.  # noqa: E501

        Number of tokens to send  # noqa: E501

        :return: The amount of this SendTokenRequestTo.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SendTokenRequestTo.

        Number of tokens to send  # noqa: E501

        :param amount: The amount of this SendTokenRequestTo.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def token_id(self):
        """Gets the token_id of this SendTokenRequestTo.  # noqa: E501

        ID of token we are sending  # noqa: E501

        :return: The token_id of this SendTokenRequestTo.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this SendTokenRequestTo.

        ID of token we are sending  # noqa: E501

        :param token_id: The token_id of this SendTokenRequestTo.  # noqa: E501
        :type: str
        """

        self._token_id = token_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SendTokenRequestTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
