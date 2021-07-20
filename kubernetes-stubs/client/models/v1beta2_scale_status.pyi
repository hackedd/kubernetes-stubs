import datetime
import typing

import kubernetes.client

class V1beta2ScaleStatus:
    replicas: int
    selector: typing.Optional[dict[str, str]]
    target_selector: typing.Optional[str]
    def __init__(
        self,
        *,
        replicas: int,
        selector: typing.Optional[dict[str, str]] = ...,
        target_selector: typing.Optional[str] = ...
    ) -> None: ...