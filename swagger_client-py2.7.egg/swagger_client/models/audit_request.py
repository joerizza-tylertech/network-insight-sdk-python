# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AuditRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'user_name': 'str',
        'ip_address': 'str',
        'entity_type': 'str',
        'entity_id': 'str',
        'operation': 'str',
        'response': 'str',
        'size': 'int',
        'cursor': 'str',
        'time_range': 'TimeRange'
    }

    attribute_map = {
        'user_name': 'user_name',
        'ip_address': 'ip_address',
        'entity_type': 'entity_type',
        'entity_id': 'entity_id',
        'operation': 'operation',
        'response': 'response',
        'size': 'size',
        'cursor': 'cursor',
        'time_range': 'time_range'
    }

    def __init__(self, user_name=None, ip_address=None, entity_type=None, entity_id=None, operation=None, response=None, size=None, cursor=None, time_range=None):
        """
        AuditRequest - a model defined in Swagger
        """

        self._user_name = None
        self._ip_address = None
        self._entity_type = None
        self._entity_id = None
        self._operation = None
        self._response = None
        self._size = None
        self._cursor = None
        self._time_range = None

        if user_name is not None:
          self.user_name = user_name
        if ip_address is not None:
          self.ip_address = ip_address
        if entity_type is not None:
          self.entity_type = entity_type
        if entity_id is not None:
          self.entity_id = entity_id
        if operation is not None:
          self.operation = operation
        if response is not None:
          self.response = response
        if size is not None:
          self.size = size
        if cursor is not None:
          self.cursor = cursor
        if time_range is not None:
          self.time_range = time_range

    @property
    def user_name(self):
        """
        Gets the user_name of this AuditRequest.

        :return: The user_name of this AuditRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this AuditRequest.

        :param user_name: The user_name of this AuditRequest.
        :type: str
        """

        self._user_name = user_name

    @property
    def ip_address(self):
        """
        Gets the ip_address of this AuditRequest.

        :return: The ip_address of this AuditRequest.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this AuditRequest.

        :param ip_address: The ip_address of this AuditRequest.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def entity_type(self):
        """
        Gets the entity_type of this AuditRequest.

        :return: The entity_type of this AuditRequest.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this AuditRequest.

        :param entity_type: The entity_type of this AuditRequest.
        :type: str
        """

        self._entity_type = entity_type

    @property
    def entity_id(self):
        """
        Gets the entity_id of this AuditRequest.

        :return: The entity_id of this AuditRequest.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this AuditRequest.

        :param entity_id: The entity_id of this AuditRequest.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def operation(self):
        """
        Gets the operation of this AuditRequest.

        :return: The operation of this AuditRequest.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this AuditRequest.

        :param operation: The operation of this AuditRequest.
        :type: str
        """

        self._operation = operation

    @property
    def response(self):
        """
        Gets the response of this AuditRequest.

        :return: The response of this AuditRequest.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """
        Sets the response of this AuditRequest.

        :param response: The response of this AuditRequest.
        :type: str
        """

        self._response = response

    @property
    def size(self):
        """
        Gets the size of this AuditRequest.

        :return: The size of this AuditRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this AuditRequest.

        :param size: The size of this AuditRequest.
        :type: int
        """

        self._size = size

    @property
    def cursor(self):
        """
        Gets the cursor of this AuditRequest.

        :return: The cursor of this AuditRequest.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this AuditRequest.

        :param cursor: The cursor of this AuditRequest.
        :type: str
        """

        self._cursor = cursor

    @property
    def time_range(self):
        """
        Gets the time_range of this AuditRequest.

        :return: The time_range of this AuditRequest.
        :rtype: TimeRange
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """
        Sets the time_range of this AuditRequest.

        :param time_range: The time_range of this AuditRequest.
        :type: TimeRange
        """

        self._time_range = time_range

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AuditRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
