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


class IpAddressRange(object):
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
        'start_ip': 'str',
        'end_ip': 'str'
    }

    attribute_map = {
        'start_ip': 'start_ip',
        'end_ip': 'end_ip'
    }

    def __init__(self, start_ip=None, end_ip=None):
        """
        IpAddressRange - a model defined in Swagger
        """

        self._start_ip = None
        self._end_ip = None

        if start_ip is not None:
          self.start_ip = start_ip
        if end_ip is not None:
          self.end_ip = end_ip

    @property
    def start_ip(self):
        """
        Gets the start_ip of this IpAddressRange.

        :return: The start_ip of this IpAddressRange.
        :rtype: str
        """
        return self._start_ip

    @start_ip.setter
    def start_ip(self, start_ip):
        """
        Sets the start_ip of this IpAddressRange.

        :param start_ip: The start_ip of this IpAddressRange.
        :type: str
        """

        self._start_ip = start_ip

    @property
    def end_ip(self):
        """
        Gets the end_ip of this IpAddressRange.

        :return: The end_ip of this IpAddressRange.
        :rtype: str
        """
        return self._end_ip

    @end_ip.setter
    def end_ip(self, end_ip):
        """
        Sets the end_ip of this IpAddressRange.

        :param end_ip: The end_ip of this IpAddressRange.
        :type: str
        """

        self._end_ip = end_ip

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
        if not isinstance(other, IpAddressRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
