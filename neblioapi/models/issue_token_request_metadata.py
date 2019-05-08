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


class IssueTokenRequestMetadata(object):
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
        'urls': 'list[IssueTokenRequestMetadataUrls]',
        'user_data': 'GetTokenMetadataResponseMetadataOfIssuenceDataUserData',
        'encryptions': 'list[IssueTokenRequestMetadataEncryptions]',
        'rules': 'IssueTokenRequestMetadataRules'
    }

    attribute_map = {
        'token_name': 'tokenName',
        'issuer': 'issuer',
        'description': 'description',
        'urls': 'urls',
        'user_data': 'userData',
        'encryptions': 'encryptions',
        'rules': 'rules'
    }

    def __init__(self, token_name=None, issuer=None, description=None, urls=None, user_data=None, encryptions=None, rules=None):  # noqa: E501
        """IssueTokenRequestMetadata - a model defined in OpenAPI"""  # noqa: E501

        self._token_name = None
        self._issuer = None
        self._description = None
        self._urls = None
        self._user_data = None
        self._encryptions = None
        self._rules = None
        self.discriminator = None

        if token_name is not None:
            self.token_name = token_name
        if issuer is not None:
            self.issuer = issuer
        if description is not None:
            self.description = description
        if urls is not None:
            self.urls = urls
        if user_data is not None:
            self.user_data = user_data
        if encryptions is not None:
            self.encryptions = encryptions
        if rules is not None:
            self.rules = rules

    @property
    def token_name(self):
        """Gets the token_name of this IssueTokenRequestMetadata.  # noqa: E501

        Token Symbol it will be identified by (ex. NIBBL)  # noqa: E501

        :return: The token_name of this IssueTokenRequestMetadata.  # noqa: E501
        :rtype: str
        """
        return self._token_name

    @token_name.setter
    def token_name(self, token_name):
        """Sets the token_name of this IssueTokenRequestMetadata.

        Token Symbol it will be identified by (ex. NIBBL)  # noqa: E501

        :param token_name: The token_name of this IssueTokenRequestMetadata.  # noqa: E501
        :type: str
        """

        self._token_name = token_name

    @property
    def issuer(self):
        """Gets the issuer of this IssueTokenRequestMetadata.  # noqa: E501

        Name of token issuer  # noqa: E501

        :return: The issuer of this IssueTokenRequestMetadata.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this IssueTokenRequestMetadata.

        Name of token issuer  # noqa: E501

        :param issuer: The issuer of this IssueTokenRequestMetadata.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def description(self):
        """Gets the description of this IssueTokenRequestMetadata.  # noqa: E501

        Long name or description of token (ex. Nibble)  # noqa: E501

        :return: The description of this IssueTokenRequestMetadata.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IssueTokenRequestMetadata.

        Long name or description of token (ex. Nibble)  # noqa: E501

        :param description: The description of this IssueTokenRequestMetadata.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def urls(self):
        """Gets the urls of this IssueTokenRequestMetadata.  # noqa: E501


        :return: The urls of this IssueTokenRequestMetadata.  # noqa: E501
        :rtype: list[IssueTokenRequestMetadataUrls]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this IssueTokenRequestMetadata.


        :param urls: The urls of this IssueTokenRequestMetadata.  # noqa: E501
        :type: list[IssueTokenRequestMetadataUrls]
        """

        self._urls = urls

    @property
    def user_data(self):
        """Gets the user_data of this IssueTokenRequestMetadata.  # noqa: E501


        :return: The user_data of this IssueTokenRequestMetadata.  # noqa: E501
        :rtype: GetTokenMetadataResponseMetadataOfIssuenceDataUserData
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this IssueTokenRequestMetadata.


        :param user_data: The user_data of this IssueTokenRequestMetadata.  # noqa: E501
        :type: GetTokenMetadataResponseMetadataOfIssuenceDataUserData
        """

        self._user_data = user_data

    @property
    def encryptions(self):
        """Gets the encryptions of this IssueTokenRequestMetadata.  # noqa: E501

        Array of encryption instruction objects for encrypting userData  # noqa: E501

        :return: The encryptions of this IssueTokenRequestMetadata.  # noqa: E501
        :rtype: list[IssueTokenRequestMetadataEncryptions]
        """
        return self._encryptions

    @encryptions.setter
    def encryptions(self, encryptions):
        """Sets the encryptions of this IssueTokenRequestMetadata.

        Array of encryption instruction objects for encrypting userData  # noqa: E501

        :param encryptions: The encryptions of this IssueTokenRequestMetadata.  # noqa: E501
        :type: list[IssueTokenRequestMetadataEncryptions]
        """

        self._encryptions = encryptions

    @property
    def rules(self):
        """Gets the rules of this IssueTokenRequestMetadata.  # noqa: E501


        :return: The rules of this IssueTokenRequestMetadata.  # noqa: E501
        :rtype: IssueTokenRequestMetadataRules
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this IssueTokenRequestMetadata.


        :param rules: The rules of this IssueTokenRequestMetadata.  # noqa: E501
        :type: IssueTokenRequestMetadataRules
        """

        self._rules = rules

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
        if not isinstance(other, IssueTokenRequestMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
