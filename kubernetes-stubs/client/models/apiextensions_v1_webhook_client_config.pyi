import datetime
import typing

import kubernetes.client

class ApiextensionsV1WebhookClientConfig:
    ca_bundle: typing.Optional[str]
    service: typing.Optional[kubernetes.client.ApiextensionsV1ServiceReference]
    url: typing.Optional[str]
    def __init__(
        self,
        *,
        ca_bundle: typing.Optional[str] = ...,
        service: typing.Optional[
            kubernetes.client.ApiextensionsV1ServiceReference
        ] = ...,
        url: typing.Optional[str] = ...
    ) -> None: ...