# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.2.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class GetTxsResponse(object):
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
        'pages_total': 'float',
        'txs': 'list[GetTxResponse]'
    }

    attribute_map = {
        'pages_total': 'pagesTotal',
        'txs': 'txs'
    }

    def __init__(self, pages_total=None, txs=None):  # noqa: E501
        """GetTxsResponse - a model defined in OpenAPI"""  # noqa: E501

        self._pages_total = None
        self._txs = None
        self.discriminator = None

        if pages_total is not None:
            self.pages_total = pages_total
        if txs is not None:
            self.txs = txs

    @property
    def pages_total(self):
        """Gets the pages_total of this GetTxsResponse.  # noqa: E501

        Number of pages of transactions  # noqa: E501

        :return: The pages_total of this GetTxsResponse.  # noqa: E501
        :rtype: float
        """
        return self._pages_total

    @pages_total.setter
    def pages_total(self, pages_total):
        """Sets the pages_total of this GetTxsResponse.

        Number of pages of transactions  # noqa: E501

        :param pages_total: The pages_total of this GetTxsResponse.  # noqa: E501
        :type: float
        """

        self._pages_total = pages_total

    @property
    def txs(self):
        """Gets the txs of this GetTxsResponse.  # noqa: E501

        Array of transaction objects  # noqa: E501

        :return: The txs of this GetTxsResponse.  # noqa: E501
        :rtype: list[GetTxResponse]
        """
        return self._txs

    @txs.setter
    def txs(self, txs):
        """Sets the txs of this GetTxsResponse.

        Array of transaction objects  # noqa: E501

        :param txs: The txs of this GetTxsResponse.  # noqa: E501
        :type: list[GetTxResponse]
        """

        self._txs = txs

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
        if not isinstance(other, GetTxsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
