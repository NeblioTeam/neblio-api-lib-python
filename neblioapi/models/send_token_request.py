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


class SendTokenRequest(object):
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
        'fee': 'float',
        '_from': 'list[str]',
        'sendutxo': 'list[str]',
        'to': 'list[SendTokenRequestTo]',
        'flags': 'IssueTokenRequestFlags',
        'metadata': 'IssueTokenRequestMetadata'
    }

    attribute_map = {
        'fee': 'fee',
        '_from': 'from',
        'sendutxo': 'sendutxo',
        'to': 'to',
        'flags': 'flags',
        'metadata': 'metadata'
    }

    def __init__(self, fee=None, _from=None, sendutxo=None, to=None, flags=None, metadata=None):  # noqa: E501
        """SendTokenRequest - a model defined in OpenAPI"""  # noqa: E501

        self._fee = None
        self.__from = None
        self._sendutxo = None
        self._to = None
        self._flags = None
        self._metadata = None
        self.discriminator = None

        self.fee = fee
        if _from is not None:
            self._from = _from
        if sendutxo is not None:
            self.sendutxo = sendutxo
        self.to = to
        if flags is not None:
            self.flags = flags
        if metadata is not None:
            self.metadata = metadata

    @property
    def fee(self):
        """Gets the fee of this SendTokenRequest.  # noqa: E501

        Fee in satoshi to include in the issuance transaction min 10000 (0.0001 NEBL)  # noqa: E501

        :return: The fee of this SendTokenRequest.  # noqa: E501
        :rtype: float
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this SendTokenRequest.

        Fee in satoshi to include in the issuance transaction min 10000 (0.0001 NEBL)  # noqa: E501

        :param fee: The fee of this SendTokenRequest.  # noqa: E501
        :type: float
        """
        if fee is None:
            raise ValueError("Invalid value for `fee`, must not be `None`")  # noqa: E501

        self._fee = fee

    @property
    def _from(self):
        """Gets the _from of this SendTokenRequest.  # noqa: E501

        Array of addresses to send the token from  # noqa: E501

        :return: The _from of this SendTokenRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this SendTokenRequest.

        Array of addresses to send the token from  # noqa: E501

        :param _from: The _from of this SendTokenRequest.  # noqa: E501
        :type: list[str]
        """

        self.__from = _from

    @property
    def sendutxo(self):
        """Gets the sendutxo of this SendTokenRequest.  # noqa: E501

        Array of UTXOs to send the token from  # noqa: E501

        :return: The sendutxo of this SendTokenRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._sendutxo

    @sendutxo.setter
    def sendutxo(self, sendutxo):
        """Sets the sendutxo of this SendTokenRequest.

        Array of UTXOs to send the token from  # noqa: E501

        :param sendutxo: The sendutxo of this SendTokenRequest.  # noqa: E501
        :type: list[str]
        """

        self._sendutxo = sendutxo

    @property
    def to(self):
        """Gets the to of this SendTokenRequest.  # noqa: E501


        :return: The to of this SendTokenRequest.  # noqa: E501
        :rtype: list[SendTokenRequestTo]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SendTokenRequest.


        :param to: The to of this SendTokenRequest.  # noqa: E501
        :type: list[SendTokenRequestTo]
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def flags(self):
        """Gets the flags of this SendTokenRequest.  # noqa: E501


        :return: The flags of this SendTokenRequest.  # noqa: E501
        :rtype: IssueTokenRequestFlags
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this SendTokenRequest.


        :param flags: The flags of this SendTokenRequest.  # noqa: E501
        :type: IssueTokenRequestFlags
        """

        self._flags = flags

    @property
    def metadata(self):
        """Gets the metadata of this SendTokenRequest.  # noqa: E501


        :return: The metadata of this SendTokenRequest.  # noqa: E501
        :rtype: IssueTokenRequestMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SendTokenRequest.


        :param metadata: The metadata of this SendTokenRequest.  # noqa: E501
        :type: IssueTokenRequestMetadata
        """

        self._metadata = metadata

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
        if not isinstance(other, SendTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
