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


class SchemaComparisonValidationResult(Model):
    """Results for schema comparison between the source and target.

    :param schema_differences: List of schema differences between the source
     and target databases
    :type schema_differences:
     ~azure.mgmt.datamigration.models.SchemaComparisonValidationResultType
    :param validation_errors: List of errors that happened while performing
     schema compare validation
    :type validation_errors: ~azure.mgmt.datamigration.models.ValidationError
    :param source_database_object_count: Count of source database objects
    :type source_database_object_count: dict[str, long]
    :param target_database_object_count: Count of target database objects
    :type target_database_object_count: dict[str, long]
    """

    _attribute_map = {
        'schema_differences': {'key': 'schemaDifferences', 'type': 'SchemaComparisonValidationResultType'},
        'validation_errors': {'key': 'validationErrors', 'type': 'ValidationError'},
        'source_database_object_count': {'key': 'sourceDatabaseObjectCount', 'type': '{long}'},
        'target_database_object_count': {'key': 'targetDatabaseObjectCount', 'type': '{long}'},
    }

    def __init__(self, schema_differences=None, validation_errors=None, source_database_object_count=None, target_database_object_count=None):
        super(SchemaComparisonValidationResult, self).__init__()
        self.schema_differences = schema_differences
        self.validation_errors = validation_errors
        self.source_database_object_count = source_database_object_count
        self.target_database_object_count = target_database_object_count