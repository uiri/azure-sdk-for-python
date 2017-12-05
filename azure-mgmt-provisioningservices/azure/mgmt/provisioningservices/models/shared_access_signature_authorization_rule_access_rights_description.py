# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SharedAccessSignatureAuthorizationRuleAccessRightsDescription(Model):
    """Description of the shared access key.

    :param key_name: Name of the key.
    :type key_name: str
    :param primary_key: Primary SAS key value.
    :type primary_key: str
    :param secondary_key: Secondary SAS key value.
    :type secondary_key: str
    :param rights: Rights that this key has. Possible values include:
     'ServiceConfig', 'EnrollmentRead', 'EnrollmentWrite', 'DeviceConnect',
     'RegistrationStatusRead', 'RegistrationStatusWrite'
    :type rights: str or
     ~azure.mgmt.provisioningservices.models.AccessRightsDescription
    """

    _validation = {
        'key_name': {'required': True},
        'rights': {'required': True},
    }

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
        'rights': {'key': 'rights', 'type': 'str'},
    }

    def __init__(self, key_name, rights, primary_key=None, secondary_key=None):
        self.key_name = key_name
        self.primary_key = primary_key
        self.secondary_key = secondary_key
        self.rights = rights
