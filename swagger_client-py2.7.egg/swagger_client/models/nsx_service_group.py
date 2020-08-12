# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NSXServiceGroup(object):
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
        'entity_id': 'str',
        'name': 'str',
        'entity_type': 'EntityType',
        'members': 'list[Reference]',
        'scope': 'ScopeEnum',
        'nsx_managers': 'list[Reference]',
        'vendor_id': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'members': 'members',
        'scope': 'scope',
        'nsx_managers': 'nsx_managers',
        'vendor_id': 'vendor_id'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, members=None, scope=None, nsx_managers=None, vendor_id=None):
        """
        NSXServiceGroup - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._members = None
        self._scope = None
        self._nsx_managers = None
        self._vendor_id = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if members is not None:
          self.members = members
        if scope is not None:
          self.scope = scope
        if nsx_managers is not None:
          self.nsx_managers = nsx_managers
        if vendor_id is not None:
          self.vendor_id = vendor_id

    @property
    def entity_id(self):
        """
        Gets the entity_id of this NSXServiceGroup.

        :return: The entity_id of this NSXServiceGroup.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this NSXServiceGroup.

        :param entity_id: The entity_id of this NSXServiceGroup.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this NSXServiceGroup.

        :return: The name of this NSXServiceGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NSXServiceGroup.

        :param name: The name of this NSXServiceGroup.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this NSXServiceGroup.

        :return: The entity_type of this NSXServiceGroup.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this NSXServiceGroup.

        :param entity_type: The entity_type of this NSXServiceGroup.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def members(self):
        """
        Gets the members of this NSXServiceGroup.

        :return: The members of this NSXServiceGroup.
        :rtype: list[Reference]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this NSXServiceGroup.

        :param members: The members of this NSXServiceGroup.
        :type: list[Reference]
        """

        self._members = members

    @property
    def scope(self):
        """
        Gets the scope of this NSXServiceGroup.

        :return: The scope of this NSXServiceGroup.
        :rtype: ScopeEnum
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this NSXServiceGroup.

        :param scope: The scope of this NSXServiceGroup.
        :type: ScopeEnum
        """

        self._scope = scope

    @property
    def nsx_managers(self):
        """
        Gets the nsx_managers of this NSXServiceGroup.

        :return: The nsx_managers of this NSXServiceGroup.
        :rtype: list[Reference]
        """
        return self._nsx_managers

    @nsx_managers.setter
    def nsx_managers(self, nsx_managers):
        """
        Sets the nsx_managers of this NSXServiceGroup.

        :param nsx_managers: The nsx_managers of this NSXServiceGroup.
        :type: list[Reference]
        """

        self._nsx_managers = nsx_managers

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this NSXServiceGroup.

        :return: The vendor_id of this NSXServiceGroup.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this NSXServiceGroup.

        :param vendor_id: The vendor_id of this NSXServiceGroup.
        :type: str
        """

        self._vendor_id = vendor_id

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
        if not isinstance(other, NSXServiceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
