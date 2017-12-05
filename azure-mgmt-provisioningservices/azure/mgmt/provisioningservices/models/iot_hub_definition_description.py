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


class IotHubDefinitionDescription(Model):
    """Description of the IoT hub.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param apply_allocation_policy: flag for applying allocationPolicy or not
     for a given iot hub.
    :type apply_allocation_policy: bool
    :param allocation_weight: weight to apply for a given iot h.
    :type allocation_weight: int
    :ivar name: Host name of the IoT hub.
    :vartype name: str
    :param connection_string: Connection string og the IoT hub.
    :type connection_string: str
    :param location: ARM region of the IoT hub.
    :type location: str
    """

    _validation = {
        'name': {'readonly': True},
        'connection_string': {'required': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'apply_allocation_policy': {'key': 'applyAllocationPolicy', 'type': 'bool'},
        'allocation_weight': {'key': 'allocationWeight', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'connection_string': {'key': 'connectionString', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, connection_string, location, apply_allocation_policy=None, allocation_weight=None):
        self.apply_allocation_policy = apply_allocation_policy
        self.allocation_weight = allocation_weight
        self.name = None
        self.connection_string = connection_string
        self.location = location
