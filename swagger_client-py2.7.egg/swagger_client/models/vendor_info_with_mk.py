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


class VendorInfoWithMk(object):
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
        'entity_type': 'str',
        'entity_name': 'str',
        'vendor_ids': 'list[VendorId]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'entity_type': 'entity_type',
        'entity_name': 'entity_name',
        'vendor_ids': 'vendor_ids'
    }

    def __init__(self, entity_id=None, entity_type=None, entity_name=None, vendor_ids=None):
        """
        VendorInfoWithMk - a model defined in Swagger
        """

        self._entity_id = None
        self._entity_type = None
        self._entity_name = None
        self._vendor_ids = None

        if entity_id is not None:
          self.entity_id = entity_id
        if entity_type is not None:
          self.entity_type = entity_type
        if entity_name is not None:
          self.entity_name = entity_name
        if vendor_ids is not None:
          self.vendor_ids = vendor_ids

    @property
    def entity_id(self):
        """
        Gets the entity_id of this VendorInfoWithMk.

        :return: The entity_id of this VendorInfoWithMk.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this VendorInfoWithMk.

        :param entity_id: The entity_id of this VendorInfoWithMk.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this VendorInfoWithMk.

        :return: The entity_type of this VendorInfoWithMk.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this VendorInfoWithMk.

        :param entity_type: The entity_type of this VendorInfoWithMk.
        :type: str
        """

        self._entity_type = entity_type

    @property
    def entity_name(self):
        """
        Gets the entity_name of this VendorInfoWithMk.

        :return: The entity_name of this VendorInfoWithMk.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this VendorInfoWithMk.

        :param entity_name: The entity_name of this VendorInfoWithMk.
        :type: str
        """

        self._entity_name = entity_name

    @property
    def vendor_ids(self):
        """
        Gets the vendor_ids of this VendorInfoWithMk.

        :return: The vendor_ids of this VendorInfoWithMk.
        :rtype: list[VendorId]
        """
        return self._vendor_ids

    @vendor_ids.setter
    def vendor_ids(self, vendor_ids):
        """
        Sets the vendor_ids of this VendorInfoWithMk.

        :param vendor_ids: The vendor_ids of this VendorInfoWithMk.
        :type: list[VendorId]
        """

        self._vendor_ids = vendor_ids

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
        if not isinstance(other, VendorInfoWithMk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
