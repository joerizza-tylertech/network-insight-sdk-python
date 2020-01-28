# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DataSourceType(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CISCOSWITCHDATASOURCE = "CiscoSwitchDataSource"
    DELLSWITCHDATASOURCE = "DellSwitchDataSource"
    ARISTASWITCHDATASOURCE = "AristaSwitchDataSource"
    BROCADESWITCHDATASOURCE = "BrocadeSwitchDataSource"
    JUNIPERSWITCHDATASOURCE = "JuniperSwitchDataSource"
    GDDATASOURCE = "GDDataSource"
    F5BIGIPDATASOURCE = "F5BIGIPDataSource"
    HUAWEISWITCHDATASOURCE = "HuaweiSwitchDataSource"
    UANIDATASOURCE = "UANIDataSource"
    VCENTERDATASOURCE = "VCenterDataSource"
    NSXVMANAGERDATASOURCE = "NSXVManagerDataSource"
    UCSMANAGERDATASOURCE = "UCSManagerDataSource"
    HPVCMANAGERDATASOURCE = "HPVCManagerDataSource"
    HPONEVIEWDATASOURCE = "HPOneViewDataSource"
    PANFIREWALLDATASOURCE = "PanFirewallDataSource"
    CHECKPOINTFIREWALLDATASOURCE = "CheckpointFirewallDataSource"
    FORTINETFIREWALLDATASOURCE = "FortinetFirewallDataSource"
    NSXTMANAGERDATASOURCE = "NSXTManagerDataSource"
    KUBERNETESDATASOURCE = "KubernetesDataSource"
    PKSDATASOURCE = "PKSDataSource"
    INFOBLOXMANAGERDATASOURCE = "InfobloxManagerDataSource"
    CISCOACIDATASOURCE = "CiscoACIDataSource"
    SERVICENOWDATASOURCE = "ServiceNowDataSource"
    POLICYMANAGERDATASOURCE = "PolicyManagerDataSource"
    AZUREDATASOURCE = "AzureDataSource"
    VELOCLOUDDATASOURCE = "VeloCloudDataSource"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        
    }

    attribute_map = {
        
    }

    def __init__(self):
        """
        DataSourceType - a model defined in Swagger
        """



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
        if not isinstance(other, DataSourceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
