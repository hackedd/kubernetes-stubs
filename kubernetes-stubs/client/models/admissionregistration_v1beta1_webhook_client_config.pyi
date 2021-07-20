import datetime
import typing

import kubernetes.client

class AdmissionregistrationV1beta1WebhookClientConfig:
    ca_bundle: typing.Optional[str]
    service: typing.Optional[
        kubernetes.client.AdmissionregistrationV1beta1ServiceReference
    ]
    url: typing.Optional[str]
    def __init__(
        self,
        *,
        ca_bundle: typing.Optional[str] = ...,
        service: typing.Optional[
            kubernetes.client.AdmissionregistrationV1beta1ServiceReference
        ] = ...,
        url: typing.Optional[str] = ...
    ) -> None: ...