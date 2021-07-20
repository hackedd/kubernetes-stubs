import datetime
import typing

import kubernetes.client

class V2beta2HorizontalPodAutoscalerSpec:
    max_replicas: int
    metrics: typing.Optional[list[kubernetes.client.V2beta2MetricSpec]]
    min_replicas: typing.Optional[int]
    scale_target_ref: kubernetes.client.V2beta2CrossVersionObjectReference
    def __init__(
        self,
        *,
        max_replicas: int,
        metrics: typing.Optional[list[kubernetes.client.V2beta2MetricSpec]] = ...,
        min_replicas: typing.Optional[int] = ...,
        scale_target_ref: kubernetes.client.V2beta2CrossVersionObjectReference
    ) -> None: ...