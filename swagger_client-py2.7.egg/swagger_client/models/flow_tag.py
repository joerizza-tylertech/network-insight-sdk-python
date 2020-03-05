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


class FlowTag(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    TRAFFIC_TYPE_UNKNOWN = "TAG_TRAFFIC_TYPE_UNKNOWN"
    INTERNET_TRAFFIC = "TAG_INTERNET_TRAFFIC"
    EAST_WEST_TRAFFIC = "TAG_EAST_WEST_TRAFFIC"
    VM_VM_TRAFFIC = "TAG_VM_VM_TRAFFIC"
    VM_PHY_TRAFFIC = "TAG_VM_PHY_TRAFFIC"
    PHY_PHY_TRAFFIC = "TAG_PHY_PHY_TRAFFIC"
    SRC_IP_VMKNIC = "TAG_SRC_IP_VMKNIC"
    DST_IP_VMKNIC = "TAG_DST_IP_VMKNIC"
    SRC_IP_VM = "TAG_SRC_IP_VM"
    DST_IP_VM = "TAG_DST_IP_VM"
    SRC_IP_INTERNET = "TAG_SRC_IP_INTERNET"
    DST_IP_INTERNET = "TAG_DST_IP_INTERNET"
    SRC_IP_PHYSICAL = "TAG_SRC_IP_PHYSICAL"
    DST_IP_PHYSICAL = "TAG_DST_IP_PHYSICAL"
    SAME_HOST = "TAG_SAME_HOST"
    DIFF_HOST = "TAG_DIFF_HOST"
    SHARED_SERVICE = "TAG_SHARED_SERVICE"
    NOT_SHARED_SERVICE = "TAG_NOT_SHARED_SERVICE"
    NETWORK_SWITCHED = "TAG_NETWORK_SWITCHED"
    NETWORK_ROUTED = "TAG_NETWORK_ROUTED"
    NETWORK_UNKNOWN = "TAG_NETWORK_UNKNOWN"
    SRC_IP_VTEP = "TAG_SRC_IP_VTEP"
    DST_IP_VTEP = "TAG_DST_IP_VTEP"
    UNICAST = "TAG_UNICAST"
    BROADCAST = "TAG_BROADCAST"
    MULTICAST = "TAG_MULTICAST"
    SRC_IP_LINK_LOCAL = "TAG_SRC_IP_LINK_LOCAL"
    DST_IP_LINK_LOCAL = "TAG_DST_IP_LINK_LOCAL"
    SRC_IP_CLASS_E = "TAG_SRC_IP_CLASS_E"
    DST_IP_CLASS_E = "TAG_DST_IP_CLASS_E"
    SRC_IP_CLASS_A_RESERVED = "TAG_SRC_IP_CLASS_A_RESERVED"
    DST_IP_CLASS_A_RESERVED = "TAG_DST_IP_CLASS_A_RESERVED"
    INVALID_IP_PACKETS = "TAG_INVALID_IP_PACKETS"
    NOT_ANALYZED = "TAG_NOT_ANALYZED"
    GENERIC_INTERNET_SRC_IP = "TAG_GENERIC_INTERNET_SRC_IP"
    SNAT_DNAT_FLOW = "TAG_SNAT_DNAT_FLOW"
    MULTINICS = "TAG_MULTINICS"
    SRC_VC = "TAG_SRC_VC"
    DST_VC = "TAG_DST_VC"
    SRC_AWS = "TAG_SRC_AWS"
    DST_AWS = "TAG_DST_AWS"
    WITHIN_DC = "TAG_WITHIN_DC"
    DIFF_DC = "TAG_DIFF_DC"
    WITHIN_VPC = "TAG_WITHIN_VPC"
    DIFF_VPC = "TAG_DIFF_VPC"
    WITHIN_VNET = "TAG_WITHIN_VNET"
    DIFF_VNET = "TAG_DIFF_VNET"
    SRC_AZURE = "TAG_SRC_AZURE"
    DST_AZURE = "TAG_DST_AZURE"

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
        FlowTag - a model defined in Swagger
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
        if not isinstance(other, FlowTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
