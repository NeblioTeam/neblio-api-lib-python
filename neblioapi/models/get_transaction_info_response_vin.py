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


class GetTransactionInfoResponseVin(object):
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
        'txid': 'str',
        'vout': 'float',
        'script_sig': 'GetTransactionInfoResponseScriptSig',
        'sequence': 'float',
        'previous_output': 'GetTransactionInfoResponsePreviousOutput',
        'tokens': 'list[GetTransactionInfoResponseTokens]',
        'value': 'float'
    }

    attribute_map = {
        'txid': 'txid',
        'vout': 'vout',
        'script_sig': 'scriptSig',
        'sequence': 'sequence',
        'previous_output': 'previousOutput',
        'tokens': 'tokens',
        'value': 'value'
    }

    def __init__(self, txid=None, vout=None, script_sig=None, sequence=None, previous_output=None, tokens=None, value=None):  # noqa: E501
        """GetTransactionInfoResponseVin - a model defined in OpenAPI"""  # noqa: E501

        self._txid = None
        self._vout = None
        self._script_sig = None
        self._sequence = None
        self._previous_output = None
        self._tokens = None
        self._value = None
        self.discriminator = None

        if txid is not None:
            self.txid = txid
        if vout is not None:
            self.vout = vout
        if script_sig is not None:
            self.script_sig = script_sig
        if sequence is not None:
            self.sequence = sequence
        if previous_output is not None:
            self.previous_output = previous_output
        if tokens is not None:
            self.tokens = tokens
        if value is not None:
            self.value = value

    @property
    def txid(self):
        """Gets the txid of this GetTransactionInfoResponseVin.  # noqa: E501

        TXID of the input  # noqa: E501

        :return: The txid of this GetTransactionInfoResponseVin.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this GetTransactionInfoResponseVin.

        TXID of the input  # noqa: E501

        :param txid: The txid of this GetTransactionInfoResponseVin.  # noqa: E501
        :type: str
        """

        self._txid = txid

    @property
    def vout(self):
        """Gets the vout of this GetTransactionInfoResponseVin.  # noqa: E501

        output index  # noqa: E501

        :return: The vout of this GetTransactionInfoResponseVin.  # noqa: E501
        :rtype: float
        """
        return self._vout

    @vout.setter
    def vout(self, vout):
        """Sets the vout of this GetTransactionInfoResponseVin.

        output index  # noqa: E501

        :param vout: The vout of this GetTransactionInfoResponseVin.  # noqa: E501
        :type: float
        """

        self._vout = vout

    @property
    def script_sig(self):
        """Gets the script_sig of this GetTransactionInfoResponseVin.  # noqa: E501


        :return: The script_sig of this GetTransactionInfoResponseVin.  # noqa: E501
        :rtype: GetTransactionInfoResponseScriptSig
        """
        return self._script_sig

    @script_sig.setter
    def script_sig(self, script_sig):
        """Sets the script_sig of this GetTransactionInfoResponseVin.


        :param script_sig: The script_sig of this GetTransactionInfoResponseVin.  # noqa: E501
        :type: GetTransactionInfoResponseScriptSig
        """

        self._script_sig = script_sig

    @property
    def sequence(self):
        """Gets the sequence of this GetTransactionInfoResponseVin.  # noqa: E501


        :return: The sequence of this GetTransactionInfoResponseVin.  # noqa: E501
        :rtype: float
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this GetTransactionInfoResponseVin.


        :param sequence: The sequence of this GetTransactionInfoResponseVin.  # noqa: E501
        :type: float
        """

        self._sequence = sequence

    @property
    def previous_output(self):
        """Gets the previous_output of this GetTransactionInfoResponseVin.  # noqa: E501


        :return: The previous_output of this GetTransactionInfoResponseVin.  # noqa: E501
        :rtype: GetTransactionInfoResponsePreviousOutput
        """
        return self._previous_output

    @previous_output.setter
    def previous_output(self, previous_output):
        """Sets the previous_output of this GetTransactionInfoResponseVin.


        :param previous_output: The previous_output of this GetTransactionInfoResponseVin.  # noqa: E501
        :type: GetTransactionInfoResponsePreviousOutput
        """

        self._previous_output = previous_output

    @property
    def tokens(self):
        """Gets the tokens of this GetTransactionInfoResponseVin.  # noqa: E501


        :return: The tokens of this GetTransactionInfoResponseVin.  # noqa: E501
        :rtype: list[GetTransactionInfoResponseTokens]
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this GetTransactionInfoResponseVin.


        :param tokens: The tokens of this GetTransactionInfoResponseVin.  # noqa: E501
        :type: list[GetTransactionInfoResponseTokens]
        """

        self._tokens = tokens

    @property
    def value(self):
        """Gets the value of this GetTransactionInfoResponseVin.  # noqa: E501

        Value of input in NEBL satoshi  # noqa: E501

        :return: The value of this GetTransactionInfoResponseVin.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GetTransactionInfoResponseVin.

        Value of input in NEBL satoshi  # noqa: E501

        :param value: The value of this GetTransactionInfoResponseVin.  # noqa: E501
        :type: float
        """

        self._value = value

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
        if not isinstance(other, GetTransactionInfoResponseVin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
