import http
from collections.abc import Generator
from typing import Any, Literal, Type, TypedDict

from _typeshed import Incomplete
from kubernetes import client as client
from urllib3 import HTTPResponse

PYDOC_RETURN_LABEL: str
PYDOC_FOLLOW_PARAM: str
TYPE_LIST_SUFFIX: str
HTTP_STATUS_GONE: Type[http.HTTPStatus.GONE]

class SimpleNamespace:
    def __init__(self, **kwargs) -> None: ...

def iter_resp_lines(resp: HTTPResponse) -> Generator[str, None, None]: ...

# TODO: Make generic?
class Event(TypedDict):
    type: str
    object: Any
    raw_object: dict

class Watch:
    resource_version: Incomplete
    def __init__(self, return_type: str | None = ...) -> None: ...
    def stop(self) -> None: ...
    def get_return_type(self, func) -> str: ...
    def get_watch_argument_name(self, func) -> Literal["follow", "watch"]: ...
    def unmarshal_event(self, data: str, return_type: str) -> Event: ...
    def stream(self, func, *args, **kwargs) -> Generator[Event, None, None]: ...
