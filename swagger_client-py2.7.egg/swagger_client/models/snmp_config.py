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


class SNMPConfig(object):
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
        'snmp_enabled': 'bool',
        'snmp_version': 'str',
        'config_snmp_2c': 'SNMP2cConfig',
        'config_snmp_3': 'SNMP3Config'
    }

    attribute_map = {
        'snmp_enabled': 'snmp_enabled',
        'snmp_version': 'snmp_version',
        'config_snmp_2c': 'config_snmp_2c',
        'config_snmp_3': 'config_snmp_3'
    }

    def __init__(self, snmp_enabled=False, snmp_version=None, config_snmp_2c=None, config_snmp_3=None):
        """
        SNMPConfig - a model defined in Swagger
        """

        self._snmp_enabled = None
        self._snmp_version = None
        self._config_snmp_2c = None
        self._config_snmp_3 = None

        if snmp_enabled is not None:
          self.snmp_enabled = snmp_enabled
        if snmp_version is not None:
          self.snmp_version = snmp_version
        if config_snmp_2c is not None:
          self.config_snmp_2c = config_snmp_2c
        if config_snmp_3 is not None:
          self.config_snmp_3 = config_snmp_3

    @property
    def snmp_enabled(self):
        """
        Gets the snmp_enabled of this SNMPConfig.

        :return: The snmp_enabled of this SNMPConfig.
        :rtype: bool
        """
        return self._snmp_enabled

    @snmp_enabled.setter
    def snmp_enabled(self, snmp_enabled):
        """
        Sets the snmp_enabled of this SNMPConfig.

        :param snmp_enabled: The snmp_enabled of this SNMPConfig.
        :type: bool
        """

        self._snmp_enabled = snmp_enabled

    @property
    def snmp_version(self):
        """
        Gets the snmp_version of this SNMPConfig.

        :return: The snmp_version of this SNMPConfig.
        :rtype: str
        """
        return self._snmp_version

    @snmp_version.setter
    def snmp_version(self, snmp_version):
        """
        Sets the snmp_version of this SNMPConfig.

        :param snmp_version: The snmp_version of this SNMPConfig.
        :type: str
        """
        allowed_values = ["v2c", "v3"]
        if snmp_version not in allowed_values:
            raise ValueError(
                "Invalid value for `snmp_version` ({0}), must be one of {1}"
                .format(snmp_version, allowed_values)
            )

        self._snmp_version = snmp_version

    @property
    def config_snmp_2c(self):
        """
        Gets the config_snmp_2c of this SNMPConfig.

        :return: The config_snmp_2c of this SNMPConfig.
        :rtype: SNMP2cConfig
        """
        return self._config_snmp_2c

    @config_snmp_2c.setter
    def config_snmp_2c(self, config_snmp_2c):
        """
        Sets the config_snmp_2c of this SNMPConfig.

        :param config_snmp_2c: The config_snmp_2c of this SNMPConfig.
        :type: SNMP2cConfig
        """

        self._config_snmp_2c = config_snmp_2c

    @property
    def config_snmp_3(self):
        """
        Gets the config_snmp_3 of this SNMPConfig.

        :return: The config_snmp_3 of this SNMPConfig.
        :rtype: SNMP3Config
        """
        return self._config_snmp_3

    @config_snmp_3.setter
    def config_snmp_3(self, config_snmp_3):
        """
        Sets the config_snmp_3 of this SNMPConfig.

        :param config_snmp_3: The config_snmp_3 of this SNMPConfig.
        :type: SNMP3Config
        """

        self._config_snmp_3 = config_snmp_3

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
        if not isinstance(other, SNMPConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other