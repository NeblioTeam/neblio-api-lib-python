# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class GetTokenHoldersResponse(object):
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
        'token_id': 'str',
        'holders': 'list[GetTokenHoldersResponseHolders]',
        'divibility': 'float',
        'lock_status': 'bool',
        'aggregation_policy': 'str',
        'some_utxo': 'str'
    }

    attribute_map = {
        'token_id': 'tokenId',
        'holders': 'holders',
        'divibility': 'divibility',
        'lock_status': 'lockStatus',
        'aggregation_policy': 'aggregationPolicy',
        'some_utxo': 'someUtxo'
    }

    def __init__(self, token_id=None, holders=None, divibility=None, lock_status=None, aggregation_policy=None, some_utxo=None):  # noqa: E501
        """GetTokenHoldersResponse - a model defined in OpenAPI"""  # noqa: E501

        self._token_id = None
        self._holders = None
        self._divibility = None
        self._lock_status = None
        self._aggregation_policy = None
        self._some_utxo = None
        self.discriminator = None

        if token_id is not None:
            self.token_id = token_id
        if holders is not None:
            self.holders = holders
        if divibility is not None:
            self.divibility = divibility
        if lock_status is not None:
            self.lock_status = lock_status
        if aggregation_policy is not None:
            self.aggregation_policy = aggregation_policy
        if some_utxo is not None:
            self.some_utxo = some_utxo

    @property
    def token_id(self):
        """Gets the token_id of this GetTokenHoldersResponse.  # noqa: E501

        TokenId of the token  # noqa: E501

        :return: The token_id of this GetTokenHoldersResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this GetTokenHoldersResponse.

        TokenId of the token  # noqa: E501

        :param token_id: The token_id of this GetTokenHoldersResponse.  # noqa: E501
        :type: str
        """

        self._token_id = token_id

    @property
    def holders(self):
        """Gets the holders of this GetTokenHoldersResponse.  # noqa: E501


        :return: The holders of this GetTokenHoldersResponse.  # noqa: E501
        :rtype: list[GetTokenHoldersResponseHolders]
        """
        return self._holders

    @holders.setter
    def holders(self, holders):
        """Sets the holders of this GetTokenHoldersResponse.


        :param holders: The holders of this GetTokenHoldersResponse.  # noqa: E501
        :type: list[GetTokenHoldersResponseHolders]
        """

        self._holders = holders

    @property
    def divibility(self):
        """Gets the divibility of this GetTokenHoldersResponse.  # noqa: E501

        How many decimal points the token is divisble to  # noqa: E501

        :return: The divibility of this GetTokenHoldersResponse.  # noqa: E501
        :rtype: float
        """
        return self._divibility

    @divibility.setter
    def divibility(self, divibility):
        """Sets the divibility of this GetTokenHoldersResponse.

        How many decimal points the token is divisble to  # noqa: E501

        :param divibility: The divibility of this GetTokenHoldersResponse.  # noqa: E501
        :type: float
        """

        self._divibility = divibility

    @property
    def lock_status(self):
        """Gets the lock_status of this GetTokenHoldersResponse.  # noqa: E501

        Whether new issuances of this token are locked  # noqa: E501

        :return: The lock_status of this GetTokenHoldersResponse.  # noqa: E501
        :rtype: bool
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        """Sets the lock_status of this GetTokenHoldersResponse.

        Whether new issuances of this token are locked  # noqa: E501

        :param lock_status: The lock_status of this GetTokenHoldersResponse.  # noqa: E501
        :type: bool
        """

        self._lock_status = lock_status

    @property
    def aggregation_policy(self):
        """Gets the aggregation_policy of this GetTokenHoldersResponse.  # noqa: E501

        Whether the tokesn are aggregatable  # noqa: E501

        :return: The aggregation_policy of this GetTokenHoldersResponse.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_policy

    @aggregation_policy.setter
    def aggregation_policy(self, aggregation_policy):
        """Sets the aggregation_policy of this GetTokenHoldersResponse.

        Whether the tokesn are aggregatable  # noqa: E501

        :param aggregation_policy: The aggregation_policy of this GetTokenHoldersResponse.  # noqa: E501
        :type: str
        """

        self._aggregation_policy = aggregation_policy

    @property
    def some_utxo(self):
        """Gets the some_utxo of this GetTokenHoldersResponse.  # noqa: E501

        A UTXO of this token  # noqa: E501

        :return: The some_utxo of this GetTokenHoldersResponse.  # noqa: E501
        :rtype: str
        """
        return self._some_utxo

    @some_utxo.setter
    def some_utxo(self, some_utxo):
        """Sets the some_utxo of this GetTokenHoldersResponse.

        A UTXO of this token  # noqa: E501

        :param some_utxo: The some_utxo of this GetTokenHoldersResponse.  # noqa: E501
        :type: str
        """

        self._some_utxo = some_utxo

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
        if not isinstance(other, GetTokenHoldersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
