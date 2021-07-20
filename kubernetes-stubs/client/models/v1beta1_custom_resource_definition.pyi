import datetime
import typing

import kubernetes.client

class V1beta1CustomResourceDefinition:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1beta1CustomResourceDefinitionSpec
    status: typing.Optional[kubernetes.client.V1beta1CustomResourceDefinitionStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1beta1CustomResourceDefinitionSpec,
        status: typing.Optional[
            kubernetes.client.V1beta1CustomResourceDefinitionStatus
        ] = ...
    ) -> None: ...