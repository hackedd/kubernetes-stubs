import datetime
import typing

import kubernetes.client

class V1beta2RollingUpdateStatefulSetStrategy:
    partition: typing.Optional[int]
    def __init__(self, *, partition: typing.Optional[int] = ...) -> None: ...