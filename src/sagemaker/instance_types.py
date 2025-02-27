# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""Accessors to retrieve instance types."""

from __future__ import absolute_import

import logging
from typing import List

from sagemaker.jumpstart import utils as jumpstart_utils
from sagemaker.jumpstart import artifacts

logger = logging.getLogger(__name__)


def retrieve_default(
    region=None,
    model_id=None,
    model_version=None,
    scope=None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> str:
    """Retrieves the default instance type for the model matching the given arguments.

    Args:
        region (str): The AWS Region for which to retrieve the default instance type.
            Defaults to ``None``.
        model_id (str): The model ID of the model for which to
            retrieve the default instance type. (Default: None).
        model_version (str): The version of the model for which to retrieve the
            default instance type. (Default: None).
        scope (str): The model type, i.e. what it is used for.
            Valid values: "training" and "inference".
        tolerate_vulnerable_model (bool): True if vulnerable versions of model
            specifications should be tolerated (exception not raised). If False, raises an
            exception if the script used by this version of the model has dependencies with known
            security vulnerabilities. (Default: False).
        tolerate_deprecated_model (bool): True if deprecated models should be tolerated
            (exception not raised). False if these models should raise an exception.
            (Default: False).
    Returns:
        str: The default instance type to use for the model.

    Raises:
        ValueError: If the combination of arguments specified is not supported.
    """
    if not jumpstart_utils.is_jumpstart_model_input(model_id, model_version):
        raise ValueError(
            "Must specify `model_id` and `model_version` when retrieving instance types."
        )

    if scope is None:
        raise ValueError("Must specify scope for instance types.")

    return artifacts._retrieve_default_instance_type(
        model_id,
        model_version,
        scope,
        region,
        tolerate_vulnerable_model,
        tolerate_deprecated_model,
    )


def retrieve(
    region=None,
    model_id=None,
    model_version=None,
    scope=None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> List[str]:
    """Retrieves the supported training instance types for the model matching the given arguments.

    Args:
        region (str): The AWS Region for which to retrieve the supported instance types.
            Defaults to ``None``.
        model_id (str): The model ID of the model for which to
            retrieve the supported instance types. (Default: None).
        model_version (str): The version of the model for which to retrieve the
            supported instance types. (Default: None).
        tolerate_vulnerable_model (bool): True if vulnerable versions of model
            specifications should be tolerated (exception not raised). If False, raises an
            exception if the script used by this version of the model has dependencies with known
            security vulnerabilities. (Default: False).
        tolerate_deprecated_model (bool): True if deprecated models should be tolerated
            (exception not raised). False if these models should raise an exception.
            (Default: False).
    Returns:
        list: The supported instance types to use for the model.

    Raises:
        ValueError: If the combination of arguments specified is not supported.
    """
    if not jumpstart_utils.is_jumpstart_model_input(model_id, model_version):
        raise ValueError(
            "Must specify `model_id` and `model_version` when retrieving instance types."
        )

    if scope is None:
        raise ValueError("Must specify scope for instance types.")

    return artifacts._retrieve_instance_types(
        model_id,
        model_version,
        scope,
        region,
        tolerate_vulnerable_model,
        tolerate_deprecated_model,
    )
