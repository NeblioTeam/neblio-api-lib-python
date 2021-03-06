# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class GetTokenMetadataResponseMetadataOfIssuanceData(object):
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
        'token_name': 'str',
        'issuer': 'str',
        'description': 'str',
        'user_data': 'GetTokenMetadataResponseMetadataOfIssuanceDataUserData'
    }

    attribute_map = {
        'token_name': 'tokenName',
        'issuer': 'issuer',
        'description': 'description',
        'user_data': 'userData'
    }

    def __init__(self, token_name=None, issuer=None, description=None, user_data=None):  # noqa: E501
        """GetTokenMetadataResponseMetadataOfIssuanceData - a model defined in OpenAPI"""  # noqa: E501

        self._token_name = None
        self._issuer = None
        self._description = None
        self._user_data = None
        self.discriminator = None

        if token_name is not None:
            self.token_name = token_name
        if issuer is not None:
            self.issuer = issuer
        if description is not None:
            self.description = description
        if user_data is not None:
            self.user_data = user_data

    @property
    def token_name(self):
        """Gets the token_name of this GetTokenMetadataResponseMetadataOfIssuanceData.  # noqa: E501

        Token symbol  # noqa: E501

        :return: The token_name of this GetTokenMetadataResponseMetadataOfIssuanceData.  # noqa: E501
        :rtype: str
        """
        return self._token_name

    @token_name.setter
    def token_name(self, token_name):
        """Sets the token_name of this GetTokenMetadataResponseMetadataOfIssuanceData.

        Token symbol  # noqa: E501

        :param token_name: The token_name of this GetTokenMetadataResponseMetadataOfIssuanceData.  # noqa: E501
        :type: str
        """

        self._token_name = token_name

    @property
    def issuer(self):
        """Gets the issuer of this GetTokenMetadataResponseMetadataOfIssuanceData.  # noqa: E501

        Name of token issuer  # noqa: E501

        :return: The issuer of this GetTokenMetadataResponseMetadataOfIssuanceData.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this GetTokenMetadataResponseMetadataOfIssuanceData.

        Name of token issuer  # noqa: E501

        :param issuer: The issuer of this GetTokenMetadataResponseMetadataOfIssuanceData.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def description(self):
        """Gets the description of this GetTokenMetadataResponseMetadataOfIssuanceData.  # noqa: E501

        Token description  # noqa: E501

        :return: The description of this GetTokenMetadataResponseMetadataOfIssuanceData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetTokenMetadataResponseMetadataOfIssuanceData.

        Token description  # noqa: E501

        :param description: The description of this GetTokenMetadataResponseMetadataOfIssuanceData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def user_data(self):
        """Gets the user_data of this GetTokenMetadataResponseMetadataOfIssuanceData.  # noqa: E501


        :return: The user_data of this GetTokenMetadataResponseMetadataOfIssuanceData.  # noqa: E501
        :rtype: GetTokenMetadataResponseMetadataOfIssuanceDataUserData
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this GetTokenMetadataResponseMetadataOfIssuanceData.


        :param user_data: The user_data of this GetTokenMetadataResponseMetadataOfIssuanceData.  # noqa: E501
        :type: GetTokenMetadataResponseMetadataOfIssuanceDataUserData
        """

        self._user_data = user_data

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
        if not isinstance(other, GetTokenMetadataResponseMetadataOfIssuanceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
