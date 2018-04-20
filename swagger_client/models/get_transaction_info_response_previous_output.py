# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetTransactionInfoResponsePreviousOutput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'asm': 'str',
        'hex': 'str',
        'req_sigs': 'float',
        'type': 'str',
        'addresses': 'list[str]'
    }

    attribute_map = {
        'asm': 'asm',
        'hex': 'hex',
        'req_sigs': 'reqSigs',
        'type': 'type',
        'addresses': 'addresses'
    }

    def __init__(self, asm=None, hex=None, req_sigs=None, type=None, addresses=None):  # noqa: E501
        """GetTransactionInfoResponsePreviousOutput - a model defined in Swagger"""  # noqa: E501

        self._asm = None
        self._hex = None
        self._req_sigs = None
        self._type = None
        self._addresses = None
        self.discriminator = None

        if asm is not None:
            self.asm = asm
        if hex is not None:
            self.hex = hex
        if req_sigs is not None:
            self.req_sigs = req_sigs
        if type is not None:
            self.type = type
        if addresses is not None:
            self.addresses = addresses

    @property
    def asm(self):
        """Gets the asm of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501


        :return: The asm of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501
        :rtype: str
        """
        return self._asm

    @asm.setter
    def asm(self, asm):
        """Sets the asm of this GetTransactionInfoResponsePreviousOutput.


        :param asm: The asm of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501
        :type: str
        """

        self._asm = asm

    @property
    def hex(self):
        """Gets the hex of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501


        :return: The hex of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501
        :rtype: str
        """
        return self._hex

    @hex.setter
    def hex(self, hex):
        """Sets the hex of this GetTransactionInfoResponsePreviousOutput.


        :param hex: The hex of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501
        :type: str
        """

        self._hex = hex

    @property
    def req_sigs(self):
        """Gets the req_sigs of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501


        :return: The req_sigs of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501
        :rtype: float
        """
        return self._req_sigs

    @req_sigs.setter
    def req_sigs(self, req_sigs):
        """Sets the req_sigs of this GetTransactionInfoResponsePreviousOutput.


        :param req_sigs: The req_sigs of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501
        :type: float
        """

        self._req_sigs = req_sigs

    @property
    def type(self):
        """Gets the type of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501


        :return: The type of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetTransactionInfoResponsePreviousOutput.


        :param type: The type of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def addresses(self):
        """Gets the addresses of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501


        :return: The addresses of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this GetTransactionInfoResponsePreviousOutput.


        :param addresses: The addresses of this GetTransactionInfoResponsePreviousOutput.  # noqa: E501
        :type: list[str]
        """

        self._addresses = addresses

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, GetTransactionInfoResponsePreviousOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
