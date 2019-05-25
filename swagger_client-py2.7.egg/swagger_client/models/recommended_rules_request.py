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


class RecommendedRulesRequest(object):
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
        'group_1': 'MicroSecGroup',
        'group_2': 'MicroSecGroup',
        'time_range': 'TimeRange'
    }

    attribute_map = {
        'group_1': 'group_1',
        'group_2': 'group_2',
        'time_range': 'time_range'
    }

    def __init__(self, group_1=None, group_2=None, time_range=None):
        """
        RecommendedRulesRequest - a model defined in Swagger
        """

        self._group_1 = None
        self._group_2 = None
        self._time_range = None

        if group_1 is not None:
          self.group_1 = group_1
        if group_2 is not None:
          self.group_2 = group_2
        if time_range is not None:
          self.time_range = time_range

    @property
    def group_1(self):
        """
        Gets the group_1 of this RecommendedRulesRequest.

        :return: The group_1 of this RecommendedRulesRequest.
        :rtype: MicroSecGroup
        """
        return self._group_1

    @group_1.setter
    def group_1(self, group_1):
        """
        Sets the group_1 of this RecommendedRulesRequest.

        :param group_1: The group_1 of this RecommendedRulesRequest.
        :type: MicroSecGroup
        """

        self._group_1 = group_1

    @property
    def group_2(self):
        """
        Gets the group_2 of this RecommendedRulesRequest.

        :return: The group_2 of this RecommendedRulesRequest.
        :rtype: MicroSecGroup
        """
        return self._group_2

    @group_2.setter
    def group_2(self, group_2):
        """
        Sets the group_2 of this RecommendedRulesRequest.

        :param group_2: The group_2 of this RecommendedRulesRequest.
        :type: MicroSecGroup
        """

        self._group_2 = group_2

    @property
    def time_range(self):
        """
        Gets the time_range of this RecommendedRulesRequest.

        :return: The time_range of this RecommendedRulesRequest.
        :rtype: TimeRange
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """
        Sets the time_range of this RecommendedRulesRequest.

        :param time_range: The time_range of this RecommendedRulesRequest.
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
        if not isinstance(other, RecommendedRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other