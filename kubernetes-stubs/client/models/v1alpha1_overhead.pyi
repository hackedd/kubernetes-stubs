import datetime
import typing

import kubernetes.client

class V1alpha1Overhead:
    pod_fixed: typing.Optional[dict[str, str]]
    def __init__(self, *, pod_fixed: typing.Optional[dict[str, str]] = ...) -> None: ...