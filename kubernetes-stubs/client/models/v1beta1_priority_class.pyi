import datetime
import typing

import kubernetes.client

class V1beta1PriorityClass:
    api_version: typing.Optional[str]
    description: typing.Optional[str]
    global_default: typing.Optional[bool]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    preemption_policy: typing.Optional[str]
    value: int
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        description: typing.Optional[str] = ...,
        global_default: typing.Optional[bool] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        preemption_policy: typing.Optional[str] = ...,
        value: int
    ) -> None: ...