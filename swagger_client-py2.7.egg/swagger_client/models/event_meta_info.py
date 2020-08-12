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


class EventMetaInfo(object):
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
        'entity_type': 'str',
        'name': 'str',
        'help_text': 'str',
        'severity': 'str',
        'tags': 'list[str]',
        'supported_entity_types': 'list[str]',
        'supported_manager_types': 'list[str]',
        'impact': 'str',
        'recommendations': 'list[str]'
    }

    attribute_map = {
        'entity_type': 'entity_type',
        'name': 'name',
        'help_text': 'help_text',
        'severity': 'severity',
        'tags': 'tags',
        'supported_entity_types': 'supported_entity_types',
        'supported_manager_types': 'supported_manager_types',
        'impact': 'impact',
        'recommendations': 'recommendations'
    }

    def __init__(self, entity_type=None, name=None, help_text=None, severity=None, tags=None, supported_entity_types=None, supported_manager_types=None, impact=None, recommendations=None):
        """
        EventMetaInfo - a model defined in Swagger
        """

        self._entity_type = None
        self._name = None
        self._help_text = None
        self._severity = None
        self._tags = None
        self._supported_entity_types = None
        self._supported_manager_types = None
        self._impact = None
        self._recommendations = None

        if entity_type is not None:
          self.entity_type = entity_type
        if name is not None:
          self.name = name
        if help_text is not None:
          self.help_text = help_text
        if severity is not None:
          self.severity = severity
        if tags is not None:
          self.tags = tags
        if supported_entity_types is not None:
          self.supported_entity_types = supported_entity_types
        if supported_manager_types is not None:
          self.supported_manager_types = supported_manager_types
        if impact is not None:
          self.impact = impact
        if recommendations is not None:
          self.recommendations = recommendations

    @property
    def entity_type(self):
        """
        Gets the entity_type of this EventMetaInfo.

        :return: The entity_type of this EventMetaInfo.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this EventMetaInfo.

        :param entity_type: The entity_type of this EventMetaInfo.
        :type: str
        """

        self._entity_type = entity_type

    @property
    def name(self):
        """
        Gets the name of this EventMetaInfo.

        :return: The name of this EventMetaInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EventMetaInfo.

        :param name: The name of this EventMetaInfo.
        :type: str
        """

        self._name = name

    @property
    def help_text(self):
        """
        Gets the help_text of this EventMetaInfo.

        :return: The help_text of this EventMetaInfo.
        :rtype: str
        """
        return self._help_text

    @help_text.setter
    def help_text(self, help_text):
        """
        Sets the help_text of this EventMetaInfo.

        :param help_text: The help_text of this EventMetaInfo.
        :type: str
        """

        self._help_text = help_text

    @property
    def severity(self):
        """
        Gets the severity of this EventMetaInfo.

        :return: The severity of this EventMetaInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this EventMetaInfo.

        :param severity: The severity of this EventMetaInfo.
        :type: str
        """
        allowed_values = ["Critical", "Warning", "Moderate", "Info"]
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def tags(self):
        """
        Gets the tags of this EventMetaInfo.

        :return: The tags of this EventMetaInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this EventMetaInfo.

        :param tags: The tags of this EventMetaInfo.
        :type: list[str]
        """

        self._tags = tags

    @property
    def supported_entity_types(self):
        """
        Gets the supported_entity_types of this EventMetaInfo.

        :return: The supported_entity_types of this EventMetaInfo.
        :rtype: list[str]
        """
        return self._supported_entity_types

    @supported_entity_types.setter
    def supported_entity_types(self, supported_entity_types):
        """
        Sets the supported_entity_types of this EventMetaInfo.

        :param supported_entity_types: The supported_entity_types of this EventMetaInfo.
        :type: list[str]
        """

        self._supported_entity_types = supported_entity_types

    @property
    def supported_manager_types(self):
        """
        Gets the supported_manager_types of this EventMetaInfo.

        :return: The supported_manager_types of this EventMetaInfo.
        :rtype: list[str]
        """
        return self._supported_manager_types

    @supported_manager_types.setter
    def supported_manager_types(self, supported_manager_types):
        """
        Sets the supported_manager_types of this EventMetaInfo.

        :param supported_manager_types: The supported_manager_types of this EventMetaInfo.
        :type: list[str]
        """

        self._supported_manager_types = supported_manager_types

    @property
    def impact(self):
        """
        Gets the impact of this EventMetaInfo.

        :return: The impact of this EventMetaInfo.
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """
        Sets the impact of this EventMetaInfo.

        :param impact: The impact of this EventMetaInfo.
        :type: str
        """
        allowed_values = ["Network Disruption Risk", "Availability Risk", "Operations", "Optimization", "Performance", "Security Risk", "Health", "Wastage", "Communication Failure", "Sync", "NA"]
        if impact not in allowed_values:
            raise ValueError(
                "Invalid value for `impact` ({0}), must be one of {1}"
                .format(impact, allowed_values)
            )

        self._impact = impact

    @property
    def recommendations(self):
        """
        Gets the recommendations of this EventMetaInfo.

        :return: The recommendations of this EventMetaInfo.
        :rtype: list[str]
        """
        return self._recommendations

    @recommendations.setter
    def recommendations(self, recommendations):
        """
        Sets the recommendations of this EventMetaInfo.

        :param recommendations: The recommendations of this EventMetaInfo.
        :type: list[str]
        """

        self._recommendations = recommendations

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
        if not isinstance(other, EventMetaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
