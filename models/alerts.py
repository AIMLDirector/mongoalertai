from pydantic import BaseModel
from typing import Dict, Any, Optional, Literal


class BaseAlert(BaseModel):
    msg: str
    c: str

    model_config = {"extra": "ignore"}


class NetworkAlert(BaseAlert):
    c: Literal["NETWORK"]
    attr: Dict[str, Any]


class QueryPerformanceAlert(BaseAlert):
    c: Literal["COMMAND"]
    attr: Dict[str, Any]


class ReplicationAlert(BaseAlert):
    c: Literal["REPL"]
    attr: Dict[str, Any]


class StorageAlert(BaseAlert):
    c: Literal["STORAGE"]
    attr: Dict[str, Any]


class AccessControlAlert(BaseAlert):
    c: Literal["ACCESS"]
    attr: Dict[str, Any]


class GenericAlert(BaseAlert):
    attr: Optional[Dict[str, Any]] = None

    model_config = {"extra": "allow"}