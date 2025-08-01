# coding: utf-8

"""
    Asteroid Agents API

    Version 1 of the Asteroid Agents API

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.execution_result import ExecutionResult
from openapi_client.models.status import Status
from typing import Optional, Set
from typing_extensions import Self

class ExecutionResultResponse(BaseModel):
    """
    ExecutionResultResponse
    """ # noqa: E501
    execution_id: StrictStr = Field(description="The ID of the execution")
    status: Status
    result: Optional[Dict[str, Any]] = Field(default=None, description="(Deprecated, use execution_result instead) The structured result data from the execution. Contains the outcome, reasoning, final answer, and result.")
    error: Optional[StrictStr] = Field(default=None, description="Error message (if execution failed)")
    execution_result: Optional[ExecutionResult] = None
    __properties: ClassVar[List[str]] = ["execution_id", "status", "result", "error", "execution_result"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ExecutionResultResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of execution_result
        if self.execution_result:
            _dict['execution_result'] = self.execution_result.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExecutionResultResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "execution_id": obj.get("execution_id"),
            "status": obj.get("status"),
            "result": obj.get("result"),
            "error": obj.get("error"),
            "execution_result": ExecutionResult.from_dict(obj["execution_result"]) if obj.get("execution_result") is not None else None
        })
        return _obj


