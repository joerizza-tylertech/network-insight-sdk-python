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


class SubscriptionRequest(object):
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
        'event_name': 'str',
        'is_problem': 'bool',
        'severity': 'str',
        'search_criteria': 'str',
        'generate_event_criteria': 'GenerateEventCritera',
        'email_frequency': 'EmailFrequency',
        'daily_at_utc': 'str',
        'email_ids': 'list[str]',
        'snmp_trap_entity_ids': 'list[str]'
    }

    attribute_map = {
        'event_name': 'event_name',
        'is_problem': 'is_problem',
        'severity': 'severity',
        'search_criteria': 'search_criteria',
        'generate_event_criteria': 'generate_event_criteria',
        'email_frequency': 'email_frequency',
        'daily_at_utc': 'daily_at_utc',
        'email_ids': 'email_ids',
        'snmp_trap_entity_ids': 'snmp_trap_entity_ids'
    }

    def __init__(self, event_name=None, is_problem=None, severity=None, search_criteria=None, generate_event_criteria=None, email_frequency=None, daily_at_utc=None, email_ids=None, snmp_trap_entity_ids=None):
        """
        SubscriptionRequest - a model defined in Swagger
        """

        self._event_name = None
        self._is_problem = None
        self._severity = None
        self._search_criteria = None
        self._generate_event_criteria = None
        self._email_frequency = None
        self._daily_at_utc = None
        self._email_ids = None
        self._snmp_trap_entity_ids = None

        if event_name is not None:
          self.event_name = event_name
        if is_problem is not None:
          self.is_problem = is_problem
        if severity is not None:
          self.severity = severity
        if search_criteria is not None:
          self.search_criteria = search_criteria
        if generate_event_criteria is not None:
          self.generate_event_criteria = generate_event_criteria
        if email_frequency is not None:
          self.email_frequency = email_frequency
        if daily_at_utc is not None:
          self.daily_at_utc = daily_at_utc
        if email_ids is not None:
          self.email_ids = email_ids
        if snmp_trap_entity_ids is not None:
          self.snmp_trap_entity_ids = snmp_trap_entity_ids

    @property
    def event_name(self):
        """
        Gets the event_name of this SubscriptionRequest.

        :return: The event_name of this SubscriptionRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this SubscriptionRequest.

        :param event_name: The event_name of this SubscriptionRequest.
        :type: str
        """

        self._event_name = event_name

    @property
    def is_problem(self):
        """
        Gets the is_problem of this SubscriptionRequest.

        :return: The is_problem of this SubscriptionRequest.
        :rtype: bool
        """
        return self._is_problem

    @is_problem.setter
    def is_problem(self, is_problem):
        """
        Sets the is_problem of this SubscriptionRequest.

        :param is_problem: The is_problem of this SubscriptionRequest.
        :type: bool
        """

        self._is_problem = is_problem

    @property
    def severity(self):
        """
        Gets the severity of this SubscriptionRequest.

        :return: The severity of this SubscriptionRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this SubscriptionRequest.

        :param severity: The severity of this SubscriptionRequest.
        :type: str
        """

        self._severity = severity

    @property
    def search_criteria(self):
        """
        Gets the search_criteria of this SubscriptionRequest.

        :return: The search_criteria of this SubscriptionRequest.
        :rtype: str
        """
        return self._search_criteria

    @search_criteria.setter
    def search_criteria(self, search_criteria):
        """
        Sets the search_criteria of this SubscriptionRequest.

        :param search_criteria: The search_criteria of this SubscriptionRequest.
        :type: str
        """

        self._search_criteria = search_criteria

    @property
    def generate_event_criteria(self):
        """
        Gets the generate_event_criteria of this SubscriptionRequest.

        :return: The generate_event_criteria of this SubscriptionRequest.
        :rtype: GenerateEventCritera
        """
        return self._generate_event_criteria

    @generate_event_criteria.setter
    def generate_event_criteria(self, generate_event_criteria):
        """
        Sets the generate_event_criteria of this SubscriptionRequest.

        :param generate_event_criteria: The generate_event_criteria of this SubscriptionRequest.
        :type: GenerateEventCritera
        """

        self._generate_event_criteria = generate_event_criteria

    @property
    def email_frequency(self):
        """
        Gets the email_frequency of this SubscriptionRequest.

        :return: The email_frequency of this SubscriptionRequest.
        :rtype: EmailFrequency
        """
        return self._email_frequency

    @email_frequency.setter
    def email_frequency(self, email_frequency):
        """
        Sets the email_frequency of this SubscriptionRequest.

        :param email_frequency: The email_frequency of this SubscriptionRequest.
        :type: EmailFrequency
        """

        self._email_frequency = email_frequency

    @property
    def daily_at_utc(self):
        """
        Gets the daily_at_utc of this SubscriptionRequest.

        :return: The daily_at_utc of this SubscriptionRequest.
        :rtype: str
        """
        return self._daily_at_utc

    @daily_at_utc.setter
    def daily_at_utc(self, daily_at_utc):
        """
        Sets the daily_at_utc of this SubscriptionRequest.

        :param daily_at_utc: The daily_at_utc of this SubscriptionRequest.
        :type: str
        """

        self._daily_at_utc = daily_at_utc

    @property
    def email_ids(self):
        """
        Gets the email_ids of this SubscriptionRequest.

        :return: The email_ids of this SubscriptionRequest.
        :rtype: list[str]
        """
        return self._email_ids

    @email_ids.setter
    def email_ids(self, email_ids):
        """
        Sets the email_ids of this SubscriptionRequest.

        :param email_ids: The email_ids of this SubscriptionRequest.
        :type: list[str]
        """

        self._email_ids = email_ids

    @property
    def snmp_trap_entity_ids(self):
        """
        Gets the snmp_trap_entity_ids of this SubscriptionRequest.

        :return: The snmp_trap_entity_ids of this SubscriptionRequest.
        :rtype: list[str]
        """
        return self._snmp_trap_entity_ids

    @snmp_trap_entity_ids.setter
    def snmp_trap_entity_ids(self, snmp_trap_entity_ids):
        """
        Sets the snmp_trap_entity_ids of this SubscriptionRequest.

        :param snmp_trap_entity_ids: The snmp_trap_entity_ids of this SubscriptionRequest.
        :type: list[str]
        """

        self._snmp_trap_entity_ids = snmp_trap_entity_ids

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
        if not isinstance(other, SubscriptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
