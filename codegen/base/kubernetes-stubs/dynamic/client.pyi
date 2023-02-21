from collections.abc import Generator
from typing import Optional, Sequence, Tuple

from _typeshed import Incomplete

from ..client.api_client import ApiClient
from ..client.configuration import Configuration
from ..watch.watch import Event, Watch
from .discovery import CacheFile, CacheVersion, Discoverer
from .discovery import EagerDiscoverer as EagerDiscoverer
from .discovery import LazyDiscoverer as LazyDiscoverer
from .resource import Resource as Resource
from .resource import ResourceField as ResourceField
from .resource import ResourceInstance as ResourceInstance
from .resource import ResourceList as ResourceList
from .resource import Subresource as Subresource

class VersionNotSupportedError(NotImplementedError): ...

Body = ResourceInstance | dict | None

class DynamicClient:
    client: ApiClient
    configuration: Optional[Configuration]
    def __init__(
        self,
        client: ApiClient,
        cache_file: CacheFile | None = ...,
        discoverer: Discoverer | None = ...,
    ) -> None: ...
    @property
    def resources(self) -> Discoverer: ...
    @property
    def version(self) -> CacheVersion: ...
    def ensure_namespace(
        self, resource: Resource, namespace: str | None, body: dict
    ) -> str: ...
    def serialize_body(self, body: Body) -> dict: ...
    def get(
        self,
        resource: Resource,
        name: str | None = ...,
        namespace: str | None = ...,
        **kwargs
    ): ...
    def create(
        self,
        resource: Resource,
        body: Body = ...,
        namespace: str | None = ...,
        **kwargs
    ): ...
    def delete(
        self,
        resource: Resource,
        name: str | None = ...,
        namespace: str | None = ...,
        body: Body = ...,
        label_selector: Incomplete | None = ...,
        field_selector: Incomplete | None = ...,
        **kwargs
    ): ...
    def replace(
        self,
        resource: Resource,
        body: Body = ...,
        name: str | None = ...,
        namespace: str | None = ...,
        **kwargs
    ): ...
    def patch(
        self,
        resource: Resource,
        body: Body = ...,
        name: str | None = ...,
        namespace: str | None = ...,
        **kwargs
    ): ...
    def server_side_apply(
        self,
        resource: Resource,
        body: Body = ...,
        name: str | None = ...,
        namespace: str | None = ...,
        force_conflicts: Incomplete | None = ...,
        **kwargs
    ): ...
    def watch(
        self,
        resource: Resource,
        namespace: str | None = ...,
        name: str | None = ...,
        label_selector: Incomplete | None = ...,
        field_selector: Incomplete | None = ...,
        resource_version: str | None = ...,
        timeout: int | None = ...,
        watcher: Watch | None = ...,
    ) -> Generator[Event, None, None]: ...
    def request(self, method: str, path: str, body: Body = ..., **params): ...
    def validate(
        self, definition: dict, version: str | None = ..., strict: bool = ...
    ) -> Tuple[Sequence[str], Sequence[str]]: ...
