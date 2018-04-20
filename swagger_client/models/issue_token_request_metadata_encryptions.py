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


class IssueTokenRequestMetadataEncryptions(object):
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
        'key': 'str',
        'pubkey': 'str',
        'format': 'str',
        'type': 'str'
    }

    attribute_map = {
        'key': 'key',
        'pubkey': 'pubkey',
        'format': 'format',
        'type': 'type'
    }

    def __init__(self, key=None, pubkey=None, format=None, type=None):  # noqa: E501
        """IssueTokenRequestMetadataEncryptions - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._pubkey = None
        self._format = None
        self._type = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if pubkey is not None:
            self.pubkey = pubkey
        if format is not None:
            self.format = format
        if type is not None:
            self.type = type

    @property
    def key(self):
        """Gets the key of this IssueTokenRequestMetadataEncryptions.  # noqa: E501

        userData key to encrypt  # noqa: E501

        :return: The key of this IssueTokenRequestMetadataEncryptions.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this IssueTokenRequestMetadataEncryptions.

        userData key to encrypt  # noqa: E501

        :param key: The key of this IssueTokenRequestMetadataEncryptions.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def pubkey(self):
        """Gets the pubkey of this IssueTokenRequestMetadataEncryptions.  # noqa: E501

        RSA public key used for encryption  # noqa: E501

        :return: The pubkey of this IssueTokenRequestMetadataEncryptions.  # noqa: E501
        :rtype: str
        """
        return self._pubkey

    @pubkey.setter
    def pubkey(self, pubkey):
        """Sets the pubkey of this IssueTokenRequestMetadataEncryptions.

        RSA public key used for encryption  # noqa: E501

        :param pubkey: The pubkey of this IssueTokenRequestMetadataEncryptions.  # noqa: E501
        :type: str
        """

        self._pubkey = pubkey

    @property
    def format(self):
        """Gets the format of this IssueTokenRequestMetadataEncryptions.  # noqa: E501

        key format (pem or der)  # noqa: E501

        :return: The format of this IssueTokenRequestMetadataEncryptions.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this IssueTokenRequestMetadataEncryptions.

        key format (pem or der)  # noqa: E501

        :param format: The format of this IssueTokenRequestMetadataEncryptions.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def type(self):
        """Gets the type of this IssueTokenRequestMetadataEncryptions.  # noqa: E501

        pkcs1 or pkcs8  # noqa: E501

        :return: The type of this IssueTokenRequestMetadataEncryptions.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IssueTokenRequestMetadataEncryptions.

        pkcs1 or pkcs8  # noqa: E501

        :param type: The type of this IssueTokenRequestMetadataEncryptions.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, IssueTokenRequestMetadataEncryptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
