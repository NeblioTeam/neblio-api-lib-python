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


class GetTxResponseVin(object):
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
        'value': 'float',
        'value_sat': 'float',
        'n': 'float'
    }

    attribute_map = {
        'txid': 'txid',
        'vout': 'vout',
        'script_sig': 'scriptSig',
        'sequence': 'sequence',
        'value': 'value',
        'value_sat': 'valueSat',
        'n': 'n'
    }

    def __init__(self, txid=None, vout=None, script_sig=None, sequence=None, value=None, value_sat=None, n=None):  # noqa: E501
        """GetTxResponseVin - a model defined in OpenAPI"""  # noqa: E501

        self._txid = None
        self._vout = None
        self._script_sig = None
        self._sequence = None
        self._value = None
        self._value_sat = None
        self._n = None
        self.discriminator = None

        if txid is not None:
            self.txid = txid
        if vout is not None:
            self.vout = vout
        if script_sig is not None:
            self.script_sig = script_sig
        if sequence is not None:
            self.sequence = sequence
        if value is not None:
            self.value = value
        if value_sat is not None:
            self.value_sat = value_sat
        if n is not None:
            self.n = n

    @property
    def txid(self):
        """Gets the txid of this GetTxResponseVin.  # noqa: E501

        TXID of the input  # noqa: E501

        :return: The txid of this GetTxResponseVin.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this GetTxResponseVin.

        TXID of the input  # noqa: E501

        :param txid: The txid of this GetTxResponseVin.  # noqa: E501
        :type: str
        """

        self._txid = txid

    @property
    def vout(self):
        """Gets the vout of this GetTxResponseVin.  # noqa: E501

        output index  # noqa: E501

        :return: The vout of this GetTxResponseVin.  # noqa: E501
        :rtype: float
        """
        return self._vout

    @vout.setter
    def vout(self, vout):
        """Sets the vout of this GetTxResponseVin.

        output index  # noqa: E501

        :param vout: The vout of this GetTxResponseVin.  # noqa: E501
        :type: float
        """

        self._vout = vout

    @property
    def script_sig(self):
        """Gets the script_sig of this GetTxResponseVin.  # noqa: E501


        :return: The script_sig of this GetTxResponseVin.  # noqa: E501
        :rtype: GetTransactionInfoResponseScriptSig
        """
        return self._script_sig

    @script_sig.setter
    def script_sig(self, script_sig):
        """Sets the script_sig of this GetTxResponseVin.


        :param script_sig: The script_sig of this GetTxResponseVin.  # noqa: E501
        :type: GetTransactionInfoResponseScriptSig
        """

        self._script_sig = script_sig

    @property
    def sequence(self):
        """Gets the sequence of this GetTxResponseVin.  # noqa: E501


        :return: The sequence of this GetTxResponseVin.  # noqa: E501
        :rtype: float
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this GetTxResponseVin.


        :param sequence: The sequence of this GetTxResponseVin.  # noqa: E501
        :type: float
        """

        self._sequence = sequence

    @property
    def value(self):
        """Gets the value of this GetTxResponseVin.  # noqa: E501

        Value of input in NEBL  # noqa: E501

        :return: The value of this GetTxResponseVin.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GetTxResponseVin.

        Value of input in NEBL  # noqa: E501

        :param value: The value of this GetTxResponseVin.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def value_sat(self):
        """Gets the value_sat of this GetTxResponseVin.  # noqa: E501

        Value of input in NEBL satoshi  # noqa: E501

        :return: The value_sat of this GetTxResponseVin.  # noqa: E501
        :rtype: float
        """
        return self._value_sat

    @value_sat.setter
    def value_sat(self, value_sat):
        """Sets the value_sat of this GetTxResponseVin.

        Value of input in NEBL satoshi  # noqa: E501

        :param value_sat: The value_sat of this GetTxResponseVin.  # noqa: E501
        :type: float
        """

        self._value_sat = value_sat

    @property
    def n(self):
        """Gets the n of this GetTxResponseVin.  # noqa: E501

        input index  # noqa: E501

        :return: The n of this GetTxResponseVin.  # noqa: E501
        :rtype: float
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this GetTxResponseVin.

        input index  # noqa: E501

        :param n: The n of this GetTxResponseVin.  # noqa: E501
        :type: float
        """

        self._n = n

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
        if not isinstance(other, GetTxResponseVin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
