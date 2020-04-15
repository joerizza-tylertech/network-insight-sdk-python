# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.settings_api import SettingsApi


class TestSettingsApi(unittest.TestCase):
    """ SettingsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.settings_api.SettingsApi()

    def tearDown(self):
        pass

    def test_add_ip_tag(self):
        """
        Test case for add_ip_tag

        Tag ip addresses with tag-id
        """
        pass

    def test_add_vidm_user(self):
        """
        Test case for add_vidm_user

        Add a VMware Identity manager user to vRealize Network Insight
        """
        pass

    def test_add_vidm_user_group(self):
        """
        Test case for add_vidm_user_group

        Add a VMware Identity Manager user-group to vRealize Network Insight
        """
        pass

    def test_create_subnet_mapping(self):
        """
        Test case for create_subnet_mapping

        Create subnet mapping
        """
        pass

    def test_delete_subnet_mapping(self):
        """
        Test case for delete_subnet_mapping

        Delete subnet mapping
        """
        pass

    def test_delete_user(self):
        """
        Test case for delete_user

        Delete an existing user.
        """
        pass

    def test_delete_user_defined_event(self):
        """
        Test case for delete_user_defined_event

        Delete an existing User defined event
        """
        pass

    def test_delete_user_group(self):
        """
        Test case for delete_user_group

        Delete an existing user-group
        """
        pass

    def test_delete_vidm_configuration(self):
        """
        Test case for delete_vidm_configuration

        Delete VMware Identity Manager configuration
        """
        pass

    def test_disable_user_defined_event(self):
        """
        Test case for disable_user_defined_event

        Disable an existing User defined event
        """
        pass

    def test_disable_vidm(self):
        """
        Test case for disable_vidm

        Disable VMware Identity Manager integration
        """
        pass

    def test_enable_user_defined_event(self):
        """
        Test case for enable_user_defined_event

        Enable an existing User defined event
        """
        pass

    def test_enable_vidm(self):
        """
        Test case for enable_vidm

        Enable VMware Identity Manager integration
        """
        pass

    def test_get_all_user_defined_events(self):
        """
        Test case for get_all_user_defined_events

        List the created User Defined Event defintions.
        """
        pass

    def test_get_ip_tag(self):
        """
        Test case for get_ip_tag

        Show ip tag details
        """
        pass

    def test_get_ip_tag_ids(self):
        """
        Test case for get_ip_tag_ids

        Show ip tag ids
        """
        pass

    def test_get_subnet_mappings(self):
        """
        Test case for get_subnet_mappings

        Get all subnet mappings
        """
        pass

    def test_get_user(self):
        """
        Test case for get_user

        Get details of a user
        """
        pass

    def test_get_user_defined_event(self):
        """
        Test case for get_user_defined_event

        Get details of an existing User defined event.
        """
        pass

    def test_get_user_group(self):
        """
        Test case for get_user_group

        Get details of a user-group
        """
        pass

    def test_get_user_groups(self):
        """
        Test case for get_user_groups

        List user-groups
        """
        pass

    def test_get_users(self):
        """
        Test case for get_users

        List the users
        """
        pass

    def test_get_vidm_configuration(self):
        """
        Test case for get_vidm_configuration

        Get configuration details of VMware Identity Manager
        """
        pass

    def test_remove_ip_tag(self):
        """
        Test case for remove_ip_tag

        Remove tag from ip addresses
        """
        pass

    def test_save_vidm_configuration(self):
        """
        Test case for save_vidm_configuration

        Configure VMware Identity Manager
        """
        pass

    def test_settings_events_user_defined_events_post(self):
        """
        Test case for settings_events_user_defined_events_post

        Add new User defined event
        """
        pass

    def test_settings_snmp_profiles_get(self):
        """
        Test case for settings_snmp_profiles_get

        List the configured SNMP destination profiles
        """
        pass

    def test_settings_snmp_profiles_id_delete(self):
        """
        Test case for settings_snmp_profiles_id_delete

        Delete an existing SNMP destination profile
        """
        pass

    def test_settings_snmp_profiles_id_get(self):
        """
        Test case for settings_snmp_profiles_id_get

        Get details of an existing SNMP destination profile
        """
        pass

    def test_settings_snmp_profiles_id_migrate_events_post(self):
        """
        Test case for settings_snmp_profiles_id_migrate_events_post

        Migrate event subscriptions to other SNMP destination profiles
        """
        pass

    def test_settings_snmp_profiles_id_put(self):
        """
        Test case for settings_snmp_profiles_id_put

        Update an existing SNMP destination profile
        """
        pass

    def test_settings_snmp_profiles_post(self):
        """
        Test case for settings_snmp_profiles_post

        Add new SNMP destination profile
        """
        pass

    def test_settings_snmp_profiles_send_test_trap_post(self):
        """
        Test case for settings_snmp_profiles_send_test_trap_post

        Send Test trap to SNMP destination profile
        """
        pass

    def test_settings_users_password_put(self):
        """
        Test case for settings_users_password_put

        Update user password
        """
        pass

    def test_update_subnet_mapping(self):
        """
        Test case for update_subnet_mapping

        Update subnet mapping
        """
        pass

    def test_update_user_defined_event(self):
        """
        Test case for update_user_defined_event

        Update an existing User defined event.
        """
        pass

    def test_update_vidm_configuration(self):
        """
        Test case for update_vidm_configuration

        Update VMware Identity Manager configuration
        """
        pass

    def test_update_vidm_user_group_role(self):
        """
        Test case for update_vidm_user_group_role

        Update role for user-group mapped through VMware Identity Manager
        """
        pass

    def test_update_vidm_user_role(self):
        """
        Test case for update_vidm_user_role

        Update role for user mapped through VMware Identity Manager
        """
        pass


if __name__ == '__main__':
    unittest.main()
