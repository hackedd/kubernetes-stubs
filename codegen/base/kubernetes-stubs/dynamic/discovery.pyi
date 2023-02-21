import abc
import json
import os
from abc import abstractmethod
from typing import Mapping, Sequence, TypedDict

from _typeshed import Incomplete
from kubernetes.client import VersionInfoDict

from .client import DynamicClient
from .exceptions import ApiException as ApiException
from .exceptions import NotFoundError as NotFoundError
from .exceptions import ResourceNotFoundError as ResourceNotFoundError
from .exceptions import ResourceNotUniqueError as ResourceNotUniqueError
from .exceptions import ServiceUnavailableError as ServiceUnavailableError
from .resource import Resource as Resource
from .resource import ResourceList as ResourceList

DISCOVERY_PREFIX: str

CacheFile = str | bytes | os.PathLike[str] | os.PathLike[bytes]

class CacheVersion(TypedDict):
    kubernetes: VersionInfoDict

class Discoverer(metaclass=abc.ABCMeta):
    client: DynamicClient
    def __init__(self, client: DynamicClient, cache_file: CacheFile | None) -> None: ...
    def invalidate_cache(self) -> None: ...
    @property
    @abc.abstractmethod
    def api_groups(self) -> Sequence[str]: ...
    @abstractmethod
    def search(
        self,
        prefix: str | None = ...,
        group: str | None = ...,
        api_version: str | None = ...,
        kind: str | None = ...,
        **kwargs
    ) -> Sequence[Resource]: ...
    @abstractmethod
    def discover(self) -> None: ...
    @property
    def version(self) -> CacheVersion: ...
    def default_groups(
        self, request_resources: bool = ...
    ) -> Mapping[str, Mapping[str, ResourceGroup]]: ...
    def parse_api_groups(
        self, request_resources: bool = ..., update: bool = ...
    ) -> Mapping[str, Mapping[str, ResourceGroup]]: ...
    def get_resources_for_api_version(
        self, prefix: str, group: str, version: str, preferred: bool
    ) -> Mapping[str, Sequence[Resource]]: ...
    def get(self, **kwargs) -> Resource: ...

class LazyDiscoverer(Discoverer):
    def __iter__(self): ...

class EagerDiscoverer(Discoverer):
    def update(self, resources: Mapping[str, Mapping[str, ResourceGroup]]) -> None: ...
    def __iter__(self): ...

class ResourceGroup:
    preferred: Incomplete
    resources: Incomplete
    def __init__(self, preferred, resources: Incomplete | None = ...) -> None: ...
    def to_dict(self): ...

class CacheEncoder(json.JSONEncoder):
    def default(self, o): ...

class CacheDecoder(json.JSONDecoder):
    client: Incomplete
    def __init__(self, client, *args, **kwargs) -> None: ...
    def object_hook(self, obj): ...
