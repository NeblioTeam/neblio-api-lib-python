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


class GetTransactionInfoResponse(object):
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
        'hex': 'str',
        'txid': 'str',
        'version': 'float',
        'locktime': 'float',
        'vin': 'list[GetTransactionInfoResponseVin]',
        'vout': 'list[GetTransactionInfoResponseVout]',
        'blocktime': 'float',
        'blockheight': 'float',
        'totalsent': 'float',
        'fee': 'float',
        'blockhash': 'str',
        'time': 'float',
        'confirmations': 'float'
    }

    attribute_map = {
        'hex': 'hex',
        'txid': 'txid',
        'version': 'version',
        'locktime': 'locktime',
        'vin': 'vin',
        'vout': 'vout',
        'blocktime': 'blocktime',
        'blockheight': 'blockheight',
        'totalsent': 'totalsent',
        'fee': 'fee',
        'blockhash': 'blockhash',
        'time': 'time',
        'confirmations': 'confirmations'
    }

    def __init__(self, hex=None, txid=None, version=None, locktime=None, vin=None, vout=None, blocktime=None, blockheight=None, totalsent=None, fee=None, blockhash=None, time=None, confirmations=None):  # noqa: E501
        """GetTransactionInfoResponse - a model defined in OpenAPI"""  # noqa: E501

        self._hex = None
        self._txid = None
        self._version = None
        self._locktime = None
        self._vin = None
        self._vout = None
        self._blocktime = None
        self._blockheight = None
        self._totalsent = None
        self._fee = None
        self._blockhash = None
        self._time = None
        self._confirmations = None
        self.discriminator = None

        if hex is not None:
            self.hex = hex
        if txid is not None:
            self.txid = txid
        if version is not None:
            self.version = version
        if locktime is not None:
            self.locktime = locktime
        if vin is not None:
            self.vin = vin
        if vout is not None:
            self.vout = vout
        if blocktime is not None:
            self.blocktime = blocktime
        if blockheight is not None:
            self.blockheight = blockheight
        if totalsent is not None:
            self.totalsent = totalsent
        if fee is not None:
            self.fee = fee
        if blockhash is not None:
            self.blockhash = blockhash
        if time is not None:
            self.time = time
        if confirmations is not None:
            self.confirmations = confirmations

    @property
    def hex(self):
        """Gets the hex of this GetTransactionInfoResponse.  # noqa: E501

        Transaction in raw hex  # noqa: E501

        :return: The hex of this GetTransactionInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._hex

    @hex.setter
    def hex(self, hex):
        """Sets the hex of this GetTransactionInfoResponse.

        Transaction in raw hex  # noqa: E501

        :param hex: The hex of this GetTransactionInfoResponse.  # noqa: E501
        :type: str
        """

        self._hex = hex

    @property
    def txid(self):
        """Gets the txid of this GetTransactionInfoResponse.  # noqa: E501

        TXID of transaction  # noqa: E501

        :return: The txid of this GetTransactionInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this GetTransactionInfoResponse.

        TXID of transaction  # noqa: E501

        :param txid: The txid of this GetTransactionInfoResponse.  # noqa: E501
        :type: str
        """

        self._txid = txid

    @property
    def version(self):
        """Gets the version of this GetTransactionInfoResponse.  # noqa: E501

        Transaction version  # noqa: E501

        :return: The version of this GetTransactionInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GetTransactionInfoResponse.

        Transaction version  # noqa: E501

        :param version: The version of this GetTransactionInfoResponse.  # noqa: E501
        :type: float
        """

        self._version = version

    @property
    def locktime(self):
        """Gets the locktime of this GetTransactionInfoResponse.  # noqa: E501

        Transaction locktime  # noqa: E501

        :return: The locktime of this GetTransactionInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._locktime

    @locktime.setter
    def locktime(self, locktime):
        """Sets the locktime of this GetTransactionInfoResponse.

        Transaction locktime  # noqa: E501

        :param locktime: The locktime of this GetTransactionInfoResponse.  # noqa: E501
        :type: float
        """

        self._locktime = locktime

    @property
    def vin(self):
        """Gets the vin of this GetTransactionInfoResponse.  # noqa: E501

        Array of transaction inputs  # noqa: E501

        :return: The vin of this GetTransactionInfoResponse.  # noqa: E501
        :rtype: list[GetTransactionInfoResponseVin]
        """
        return self._vin

    @vin.setter
    def vin(self, vin):
        """Sets the vin of this GetTransactionInfoResponse.

        Array of transaction inputs  # noqa: E501

        :param vin: The vin of this GetTransactionInfoResponse.  # noqa: E501
        :type: list[GetTransactionInfoResponseVin]
        """

        self._vin = vin

    @property
    def vout(self):
        """Gets the vout of this GetTransactionInfoResponse.  # noqa: E501

        Array of transaction outputs  # noqa: E501

        :return: The vout of this GetTransactionInfoResponse.  # noqa: E501
        :rtype: list[GetTransactionInfoResponseVout]
        """
        return self._vout

    @vout.setter
    def vout(self, vout):
        """Sets the vout of this GetTransactionInfoResponse.

        Array of transaction outputs  # noqa: E501

        :param vout: The vout of this GetTransactionInfoResponse.  # noqa: E501
        :type: list[GetTransactionInfoResponseVout]
        """

        self._vout = vout

    @property
    def blocktime(self):
        """Gets the blocktime of this GetTransactionInfoResponse.  # noqa: E501

        Block time of this transaction  # noqa: E501

        :return: The blocktime of this GetTransactionInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._blocktime

    @blocktime.setter
    def blocktime(self, blocktime):
        """Sets the blocktime of this GetTransactionInfoResponse.

        Block time of this transaction  # noqa: E501

        :param blocktime: The blocktime of this GetTransactionInfoResponse.  # noqa: E501
        :type: float
        """

        self._blocktime = blocktime

    @property
    def blockheight(self):
        """Gets the blockheight of this GetTransactionInfoResponse.  # noqa: E501

        Block height of this transaction  # noqa: E501

        :return: The blockheight of this GetTransactionInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._blockheight

    @blockheight.setter
    def blockheight(self, blockheight):
        """Sets the blockheight of this GetTransactionInfoResponse.

        Block height of this transaction  # noqa: E501

        :param blockheight: The blockheight of this GetTransactionInfoResponse.  # noqa: E501
        :type: float
        """

        self._blockheight = blockheight

    @property
    def totalsent(self):
        """Gets the totalsent of this GetTransactionInfoResponse.  # noqa: E501

        Total NEBL sent in this transaction in satoshis  # noqa: E501

        :return: The totalsent of this GetTransactionInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._totalsent

    @totalsent.setter
    def totalsent(self, totalsent):
        """Sets the totalsent of this GetTransactionInfoResponse.

        Total NEBL sent in this transaction in satoshis  # noqa: E501

        :param totalsent: The totalsent of this GetTransactionInfoResponse.  # noqa: E501
        :type: float
        """

        self._totalsent = totalsent

    @property
    def fee(self):
        """Gets the fee of this GetTransactionInfoResponse.  # noqa: E501

        Total NEBL used as fee for this transcation in satoshis  # noqa: E501

        :return: The fee of this GetTransactionInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this GetTransactionInfoResponse.

        Total NEBL used as fee for this transcation in satoshis  # noqa: E501

        :param fee: The fee of this GetTransactionInfoResponse.  # noqa: E501
        :type: float
        """

        self._fee = fee

    @property
    def blockhash(self):
        """Gets the blockhash of this GetTransactionInfoResponse.  # noqa: E501

        Hash of the block this transaction is in  # noqa: E501

        :return: The blockhash of this GetTransactionInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._blockhash

    @blockhash.setter
    def blockhash(self, blockhash):
        """Sets the blockhash of this GetTransactionInfoResponse.

        Hash of the block this transaction is in  # noqa: E501

        :param blockhash: The blockhash of this GetTransactionInfoResponse.  # noqa: E501
        :type: str
        """

        self._blockhash = blockhash

    @property
    def time(self):
        """Gets the time of this GetTransactionInfoResponse.  # noqa: E501

        Transaction time  # noqa: E501

        :return: The time of this GetTransactionInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this GetTransactionInfoResponse.

        Transaction time  # noqa: E501

        :param time: The time of this GetTransactionInfoResponse.  # noqa: E501
        :type: float
        """

        self._time = time

    @property
    def confirmations(self):
        """Gets the confirmations of this GetTransactionInfoResponse.  # noqa: E501

        Number of transaction confirmations  # noqa: E501

        :return: The confirmations of this GetTransactionInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._confirmations

    @confirmations.setter
    def confirmations(self, confirmations):
        """Sets the confirmations of this GetTransactionInfoResponse.

        Number of transaction confirmations  # noqa: E501

        :param confirmations: The confirmations of this GetTransactionInfoResponse.  # noqa: E501
        :type: float
        """

        self._confirmations = confirmations

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
        if not isinstance(other, GetTransactionInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
