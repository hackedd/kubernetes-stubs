import datetime
import typing

import kubernetes.client

class V1beta2RollingUpdateDaemonSet:
    max_unavailable: typing.Optional[typing.Any]
    def __init__(
        self, *, max_unavailable: typing.Optional[typing.Any] = ...
    ) -> None: ...