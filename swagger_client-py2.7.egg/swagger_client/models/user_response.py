# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserResponse(object):
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
        'user_type': 'UserType',
        'id': 'str',
        'role': 'Role',
        'username': 'str',
        'domain': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'user_type': 'user_type',
        'id': 'id',
        'role': 'role',
        'username': 'username',
        'domain': 'domain',
        'display_name': 'display_name'
    }

    def __init__(self, user_type=None, id=None, role=None, username=None, domain=None, display_name=None):
        """
        UserResponse - a model defined in Swagger
        """

        self._user_type = None
        self._id = None
        self._role = None
        self._username = None
        self._domain = None
        self._display_name = None

        if user_type is not None:
          self.user_type = user_type
        if id is not None:
          self.id = id
        if role is not None:
          self.role = role
        if username is not None:
          self.username = username
        if domain is not None:
          self.domain = domain
        if display_name is not None:
          self.display_name = display_name

    @property
    def user_type(self):
        """
        Gets the user_type of this UserResponse.

        :return: The user_type of this UserResponse.
        :rtype: UserType
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """
        Sets the user_type of this UserResponse.

        :param user_type: The user_type of this UserResponse.
        :type: UserType
        """

        self._user_type = user_type

    @property
    def id(self):
        """
        Gets the id of this UserResponse.
        Unique identifier assigned to user.

        :return: The id of this UserResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserResponse.
        Unique identifier assigned to user.

        :param id: The id of this UserResponse.
        :type: str
        """

        self._id = id

    @property
    def role(self):
        """
        Gets the role of this UserResponse.

        :return: The role of this UserResponse.
        :rtype: Role
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this UserResponse.

        :param role: The role of this UserResponse.
        :type: Role
        """

        self._role = role

    @property
    def username(self):
        """
        Gets the username of this UserResponse.
        Username of the user

        :return: The username of this UserResponse.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserResponse.
        Username of the user

        :param username: The username of this UserResponse.
        :type: str
        """

        self._username = username

    @property
    def domain(self):
        """
        Gets the domain of this UserResponse.
        Domain name to which group belongs to.

        :return: The domain of this UserResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this UserResponse.
        Domain name to which group belongs to.

        :param domain: The domain of this UserResponse.
        :type: str
        """

        self._domain = domain

    @property
    def display_name(self):
        """
        Gets the display_name of this UserResponse.
        User's display name

        :return: The display_name of this UserResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UserResponse.
        User's display name

        :param display_name: The display_name of this UserResponse.
        :type: str
        """

        self._display_name = display_name

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
        if not isinstance(other, UserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
