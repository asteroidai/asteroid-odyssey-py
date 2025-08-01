# coding: utf-8

"""
    Asteroid Agents API

    Version 1 of the Asteroid Agents API

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Status(str, Enum):
    """
    Status of the execution
    """

    """
    allowed enum values
    """
    STARTING = 'starting'
    RUNNING = 'running'
    PAUSED = 'paused'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    FAILED = 'failed'
    AWAITING_COMPLETION = 'awaiting_completion'
    PAUSED_BY_AGENT = 'paused_by_agent'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Status from a JSON string"""
        return cls(json.loads(json_str))


