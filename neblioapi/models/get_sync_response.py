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


class GetSyncResponse(object):
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
        'status': 'str',
        'block_chain_height': 'float',
        'sync_percentage': 'float',
        'height': 'float',
        'error': 'str',
        'type': 'str'
    }

    attribute_map = {
        'status': 'status',
        'block_chain_height': 'blockChainHeight',
        'sync_percentage': 'syncPercentage',
        'height': 'height',
        'error': 'error',
        'type': 'type'
    }

    def __init__(self, status=None, block_chain_height=None, sync_percentage=None, height=None, error=None, type=None):  # noqa: E501
        """GetSyncResponse - a model defined in OpenAPI"""  # noqa: E501

        self._status = None
        self._block_chain_height = None
        self._sync_percentage = None
        self._height = None
        self._error = None
        self._type = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if block_chain_height is not None:
            self.block_chain_height = block_chain_height
        if sync_percentage is not None:
            self.sync_percentage = sync_percentage
        if height is not None:
            self.height = height
        if error is not None:
            self.error = error
        if type is not None:
            self.type = type

    @property
    def status(self):
        """Gets the status of this GetSyncResponse.  # noqa: E501

        Current sync status  # noqa: E501

        :return: The status of this GetSyncResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetSyncResponse.

        Current sync status  # noqa: E501

        :param status: The status of this GetSyncResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def block_chain_height(self):
        """Gets the block_chain_height of this GetSyncResponse.  # noqa: E501

        Current blockchain height  # noqa: E501

        :return: The block_chain_height of this GetSyncResponse.  # noqa: E501
        :rtype: float
        """
        return self._block_chain_height

    @block_chain_height.setter
    def block_chain_height(self, block_chain_height):
        """Sets the block_chain_height of this GetSyncResponse.

        Current blockchain height  # noqa: E501

        :param block_chain_height: The block_chain_height of this GetSyncResponse.  # noqa: E501
        :type: float
        """

        self._block_chain_height = block_chain_height

    @property
    def sync_percentage(self):
        """Gets the sync_percentage of this GetSyncResponse.  # noqa: E501

        Current sync percentage  # noqa: E501

        :return: The sync_percentage of this GetSyncResponse.  # noqa: E501
        :rtype: float
        """
        return self._sync_percentage

    @sync_percentage.setter
    def sync_percentage(self, sync_percentage):
        """Sets the sync_percentage of this GetSyncResponse.

        Current sync percentage  # noqa: E501

        :param sync_percentage: The sync_percentage of this GetSyncResponse.  # noqa: E501
        :type: float
        """

        self._sync_percentage = sync_percentage

    @property
    def height(self):
        """Gets the height of this GetSyncResponse.  # noqa: E501

        Height node is synced to  # noqa: E501

        :return: The height of this GetSyncResponse.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this GetSyncResponse.

        Height node is synced to  # noqa: E501

        :param height: The height of this GetSyncResponse.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def error(self):
        """Gets the error of this GetSyncResponse.  # noqa: E501

        Recent sync error messages  # noqa: E501

        :return: The error of this GetSyncResponse.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this GetSyncResponse.

        Recent sync error messages  # noqa: E501

        :param error: The error of this GetSyncResponse.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def type(self):
        """Gets the type of this GetSyncResponse.  # noqa: E501

        Node type  # noqa: E501

        :return: The type of this GetSyncResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetSyncResponse.

        Node type  # noqa: E501

        :param type: The type of this GetSyncResponse.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, GetSyncResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
