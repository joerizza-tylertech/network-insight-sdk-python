# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.application_api import ApplicationApi


class TestApplicationApi(unittest.TestCase):
    """ ApplicationApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.application_api.ApplicationApi()

    def tearDown(self):
        pass

    def test_get_applications_members(self):
        """
        Test case for get_applications_members

        Get member details of applications
        """
        pass

    def test_get_tiers_members(self):
        """
        Test case for get_tiers_members

        Get member details of tiers
        """
        pass


if __name__ == '__main__':
    unittest.main()