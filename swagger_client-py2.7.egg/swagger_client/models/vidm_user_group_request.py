# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VidmUserGroupRequest(object):
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
        'group_name': 'str',
        'domain': 'str',
        'role': 'Role'
    }

    attribute_map = {
        'group_name': 'group_name',
        'domain': 'domain',
        'role': 'role'
    }

    def __init__(self, group_name=None, domain=None, role=None):
        """
        VidmUserGroupRequest - a model defined in Swagger
        """

        self._group_name = None
        self._domain = None
        self._role = None

        if group_name is not None:
          self.group_name = group_name
        if domain is not None:
          self.domain = domain
        if role is not None:
          self.role = role

    @property
    def group_name(self):
        """
        Gets the group_name of this VidmUserGroupRequest.
        Specify group name (domain should not be part of group name).

        :return: The group_name of this VidmUserGroupRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this VidmUserGroupRequest.
        Specify group name (domain should not be part of group name).

        :param group_name: The group_name of this VidmUserGroupRequest.
        :type: str
        """

        self._group_name = group_name

    @property
    def domain(self):
        """
        Gets the domain of this VidmUserGroupRequest.
        Provide domain name to which user-group belongs to.

        :return: The domain of this VidmUserGroupRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this VidmUserGroupRequest.
        Provide domain name to which user-group belongs to.

        :param domain: The domain of this VidmUserGroupRequest.
        :type: str
        """

        self._domain = domain

    @property
    def role(self):
        """
        Gets the role of this VidmUserGroupRequest.

        :return: The role of this VidmUserGroupRequest.
        :rtype: Role
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this VidmUserGroupRequest.

        :param role: The role of this VidmUserGroupRequest.
        :type: Role
        """

        self._role = role

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
        if not isinstance(other, VidmUserGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other