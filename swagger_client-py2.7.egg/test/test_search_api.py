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
from swagger_client.apis.search_api import SearchApi


class TestSearchApi(unittest.TestCase):
    """ SearchApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.search_api.SearchApi()

    def tearDown(self):
        pass

    def test_aggregate_search_results(self):
        """
        Test case for aggregate_search_results

        Aggregation API
        """
        pass

    def test_group_search_results(self):
        """
        Test case for group_search_results

        Groupby Search API
        """
        pass

    def test_search_entities(self):
        """
        Test case for search_entities

        Search entities
        """
        pass


if __name__ == '__main__':
    unittest.main()
