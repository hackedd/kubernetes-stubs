from typing import Any, Mapping, Optional, TypedDict

from _typeshed import Incomplete

class ResourceUrls(TypedDict):
    base: str
    namespaced_base: str
    full: str
    namespaced_full: str

class Resource:
    prefix: Optional[str]
    group: Optional[str]
    api_version: Optional[str]
    kind: Optional[str]
    namespaced: bool
    verbs: Incomplete
    name: Optional[str]
    preferred: Incomplete
    client: Incomplete
    singular_name: Optional[str]
    short_names: Incomplete
    categories: Incomplete
    subresources: dict[str, "Subresource"]
    extra_args: Incomplete
    def __init__(
        self,
        prefix: str | None = ...,
        group: str | None = ...,
        api_version: str | None = ...,
        kind: str | None = ...,
        namespaced: bool = ...,
        verbs: Incomplete | None = ...,
        name: str | None = ...,
        preferred: bool = ...,
        client: Incomplete | None = ...,
        singularName: str | None = ...,
        shortNames: Incomplete | None = ...,
        categories: Incomplete | None = ...,
        subresources: Mapping[str, Mapping[str, Any]] | None = ...,
        **kwargs
    ) -> None: ...
    def to_dict(self) -> dict: ...
    @property
    def group_version(self) -> str: ...
    @property
    def urls(self) -> ResourceUrls: ...
    def path(self, name: Optional[str] = ..., namespace: Optional[str] = ...): ...
    # def __getattr__(self, name: str): ...

class ResourceList(Resource):
    base_kind: Optional[str]
    base_resource_lookup: Incomplete
    def __init__(
        self,
        client,
        group: str = ...,
        api_version: str = ...,
        base_kind: str = ...,
        kind: Incomplete | None = ...,
        base_resource_lookup: Incomplete | None = ...,
    ) -> None: ...
    def base_resource(self) -> Resource | None: ...
    def get(
        self,
        body,
        name: Incomplete | None = ...,
        namespace: Incomplete | None = ...,
        **kwargs
    ) -> ResourceInstance: ...
    def delete(
        self,
        body,
        name: Incomplete | None = ...,
        namespace: Incomplete | None = ...,
        **kwargs
    ) -> ResourceInstance: ...
    def verb_mapper(self, verb, body, **kwargs) -> ResourceInstance: ...
    def create(self, *args, **kwargs) -> ResourceInstance: ...
    def replace(self, *args, **kwargs) -> ResourceInstance: ...
    def patch(self, *args, **kwargs) -> ResourceInstance: ...
    def to_dict(self) -> dict: ...
    # def __getattr__(self, name): ...

class SubresourceUrls(TypedDict):
    full: str
    namespaced_full: str

class Subresource(Resource):
    parent: Incomplete
    prefix: Incomplete
    group: Incomplete
    api_version: Incomplete
    kind: Incomplete
    name: Incomplete
    subresource: Incomplete
    namespaced: Incomplete
    verbs: Incomplete
    extra_args: Incomplete
    def __init__(self, parent, **kwargs) -> None: ...
    def create(
        self,
        body: Incomplete | None = ...,
        name: Incomplete | None = ...,
        namespace: Incomplete | None = ...,
        **kwargs
    ): ...
    @property
    def urls(self) -> SubresourceUrls: ...
    # def __getattr__(self, name): ...
    def to_dict(self) -> dict: ...

class ResourceInstance:
    client: Incomplete
    attributes: Incomplete
    def __init__(self, client, instance) -> None: ...
    def to_dict(self) -> dict: ...
    def to_str(self) -> str: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...
    def __getitem__(self, name): ...
    def __setitem__(self, name, value) -> None: ...
    def __dir__(self): ...

class ResourceField:
    def __init__(self, params: dict[str, Any]) -> None: ...
    def __eq__(self, other): ...
    def __getitem__(self, name): ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value) -> None: ...
    def __dir__(self): ...
    def __iter__(self): ...
