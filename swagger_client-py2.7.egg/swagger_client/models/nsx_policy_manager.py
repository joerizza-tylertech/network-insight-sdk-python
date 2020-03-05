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


class NSXPolicyManager(object):
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
        'ip_address': 'IpV4Address',
        'data_source': 'Reference',
        'fqdn': 'str',
        'enforcement_points': 'list[Reference]',
        'sddc_type': 'SddcType',
        'sddc': 'Reference'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'ip_address': 'ip_address',
        'data_source': 'data_source',
        'fqdn': 'fqdn',
        'enforcement_points': 'enforcement_points',
        'sddc_type': 'sddc_type',
        'sddc': 'sddc'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, ip_address=None, data_source=None, fqdn=None, enforcement_points=None, sddc_type=None, sddc=None):
        """
        NSXPolicyManager - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._ip_address = None
        self._data_source = None
        self._fqdn = None
        self._enforcement_points = None
        self._sddc_type = None
        self._sddc = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if ip_address is not None:
          self.ip_address = ip_address
        if data_source is not None:
          self.data_source = data_source
        if fqdn is not None:
          self.fqdn = fqdn
        if enforcement_points is not None:
          self.enforcement_points = enforcement_points
        if sddc_type is not None:
          self.sddc_type = sddc_type
        if sddc is not None:
          self.sddc = sddc

    @property
    def entity_id(self):
        """
        Gets the entity_id of this NSXPolicyManager.

        :return: The entity_id of this NSXPolicyManager.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this NSXPolicyManager.

        :param entity_id: The entity_id of this NSXPolicyManager.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this NSXPolicyManager.

        :return: The name of this NSXPolicyManager.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NSXPolicyManager.

        :param name: The name of this NSXPolicyManager.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this NSXPolicyManager.

        :return: The entity_type of this NSXPolicyManager.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this NSXPolicyManager.

        :param entity_type: The entity_type of this NSXPolicyManager.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def ip_address(self):
        """
        Gets the ip_address of this NSXPolicyManager.

        :return: The ip_address of this NSXPolicyManager.
        :rtype: IpV4Address
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this NSXPolicyManager.

        :param ip_address: The ip_address of this NSXPolicyManager.
        :type: IpV4Address
        """

        self._ip_address = ip_address

    @property
    def data_source(self):
        """
        Gets the data_source of this NSXPolicyManager.

        :return: The data_source of this NSXPolicyManager.
        :rtype: Reference
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """
        Sets the data_source of this NSXPolicyManager.

        :param data_source: The data_source of this NSXPolicyManager.
        :type: Reference
        """

        self._data_source = data_source

    @property
    def fqdn(self):
        """
        Gets the fqdn of this NSXPolicyManager.

        :return: The fqdn of this NSXPolicyManager.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this NSXPolicyManager.

        :param fqdn: The fqdn of this NSXPolicyManager.
        :type: str
        """

        self._fqdn = fqdn

    @property
    def enforcement_points(self):
        """
        Gets the enforcement_points of this NSXPolicyManager.

        :return: The enforcement_points of this NSXPolicyManager.
        :rtype: list[Reference]
        """
        return self._enforcement_points

    @enforcement_points.setter
    def enforcement_points(self, enforcement_points):
        """
        Sets the enforcement_points of this NSXPolicyManager.

        :param enforcement_points: The enforcement_points of this NSXPolicyManager.
        :type: list[Reference]
        """

        self._enforcement_points = enforcement_points

    @property
    def sddc_type(self):
        """
        Gets the sddc_type of this NSXPolicyManager.

        :return: The sddc_type of this NSXPolicyManager.
        :rtype: SddcType
        """
        return self._sddc_type

    @sddc_type.setter
    def sddc_type(self, sddc_type):
        """
        Sets the sddc_type of this NSXPolicyManager.

        :param sddc_type: The sddc_type of this NSXPolicyManager.
        :type: SddcType
        """

        self._sddc_type = sddc_type

    @property
    def sddc(self):
        """
        Gets the sddc of this NSXPolicyManager.

        :return: The sddc of this NSXPolicyManager.
        :rtype: Reference
        """
        return self._sddc

    @sddc.setter
    def sddc(self, sddc):
        """
        Sets the sddc of this NSXPolicyManager.

        :param sddc: The sddc of this NSXPolicyManager.
        :type: Reference
        """

        self._sddc = sddc

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
        if not isinstance(other, NSXPolicyManager):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
