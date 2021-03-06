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


class VerifyRequest(Model):
    """Request body for verify operation.

    :param face_id: faceId the face, comes from Face - Detect
    :type face_id: str
    :param person_id: Specify a certain person in a person group. personId is
     created in Persons.Create.
    :type person_id: str
    :param person_group_id: Using existing personGroupId and personId for fast
     loading a specified person. personGroupId is created in Person
     Groups.Create.
    :type person_group_id: str
    """

    _validation = {
        'face_id': {'required': True, 'max_length': 64},
        'person_id': {'required': True},
        'person_group_id': {'required': True},
    }

    _attribute_map = {
        'face_id': {'key': 'faceId', 'type': 'str'},
        'person_id': {'key': 'personId', 'type': 'str'},
        'person_group_id': {'key': 'personGroupId', 'type': 'str'},
    }

    def __init__(self, face_id, person_id, person_group_id):
        self.face_id = face_id
        self.person_id = person_id
        self.person_group_id = person_group_id
