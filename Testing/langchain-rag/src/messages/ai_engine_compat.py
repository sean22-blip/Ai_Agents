from enum import Enum
from typing import List, Optional
from uagents import Model


class UAgentResponseType(str, Enum):
    FINAL = "final"
    ERROR = "error"
    VALIDATION_ERROR = "validation_error"
    SELECT_FROM_OPTIONS = "select_from_options"
    FINAL_OPTIONS = "final_options"


class KeyValue(Model):
    key: str
    value: str


class UAgentResponse(Model):
    version: str = "v1"
    type: UAgentResponseType
    request_id: Optional[str] = None
    agent_address: Optional[str] = None
    message: Optional[str] = None
    options: Optional[List[KeyValue]] = None
    verbose_message: Optional[str] = None
    verbose_options: Optional[List[KeyValue]] = None