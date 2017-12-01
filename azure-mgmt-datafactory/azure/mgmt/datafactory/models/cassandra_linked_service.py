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

from .linked_service import LinkedService


class CassandraLinkedService(LinkedService):
    """Linked service for Cassandra data source.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param type: Constant filled by server.
    :type type: str
    :param host: Host name for connection. Type: string (or Expression with
     resultType string).
    :type host: object
    :param authentication_type: AuthenticationType to be used for connection.
     Type: string (or Expression with resultType string).
    :type authentication_type: object
    :param port: The port for the connection. Type: integer (or Expression
     with resultType integer).
    :type port: object
    :param username: Username for authentication. Type: string (or Expression
     with resultType string).
    :type username: object
    :param password: Password for authentication.
    :type password: ~azure.mgmt.datafactory.models.SecureString
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'host': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'host': {'key': 'typeProperties.host', 'type': 'object'},
        'authentication_type': {'key': 'typeProperties.authenticationType', 'type': 'object'},
        'port': {'key': 'typeProperties.port', 'type': 'object'},
        'username': {'key': 'typeProperties.username', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecureString'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, host, additional_properties=None, connect_via=None, description=None, authentication_type=None, port=None, username=None, password=None, encrypted_credential=None):
        super(CassandraLinkedService, self).__init__(additional_properties=additional_properties, connect_via=connect_via, description=description)
        self.host = host
        self.authentication_type = authentication_type
        self.port = port
        self.username = username
        self.password = password
        self.encrypted_credential = encrypted_credential
        self.type = 'Cassandra'
