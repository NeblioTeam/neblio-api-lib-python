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


class GetRawTxResponse(object):
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
        'rawtx': 'str'
    }

    attribute_map = {
        'rawtx': 'rawtx'
    }

    def __init__(self, rawtx=None):  # noqa: E501
        """GetRawTxResponse - a model defined in OpenAPI"""  # noqa: E501

        self._rawtx = None
        self.discriminator = None

        if rawtx is not None:
            self.rawtx = rawtx

    @property
    def rawtx(self):
        """Gets the rawtx of this GetRawTxResponse.  # noqa: E501

        Raw hex representing the transaction  # noqa: E501

        :return: The rawtx of this GetRawTxResponse.  # noqa: E501
        :rtype: str
        """
        return self._rawtx

    @rawtx.setter
    def rawtx(self, rawtx):
        """Sets the rawtx of this GetRawTxResponse.

        Raw hex representing the transaction  # noqa: E501

        :param rawtx: The rawtx of this GetRawTxResponse.  # noqa: E501
        :type: str
        """

        self._rawtx = rawtx

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
        if not isinstance(other, GetRawTxResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
