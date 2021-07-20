import datetime
import typing

import kubernetes.client

class V1SecurityContext:
    allow_privilege_escalation: typing.Optional[bool]
    capabilities: typing.Optional[kubernetes.client.V1Capabilities]
    privileged: typing.Optional[bool]
    proc_mount: typing.Optional[str]
    read_only_root_filesystem: typing.Optional[bool]
    run_as_group: typing.Optional[int]
    run_as_non_root: typing.Optional[bool]
    run_as_user: typing.Optional[int]
    se_linux_options: typing.Optional[kubernetes.client.V1SELinuxOptions]
    windows_options: typing.Optional[kubernetes.client.V1WindowsSecurityContextOptions]
    def __init__(
        self,
        *,
        allow_privilege_escalation: typing.Optional[bool] = ...,
        capabilities: typing.Optional[kubernetes.client.V1Capabilities] = ...,
        privileged: typing.Optional[bool] = ...,
        proc_mount: typing.Optional[str] = ...,
        read_only_root_filesystem: typing.Optional[bool] = ...,
        run_as_group: typing.Optional[int] = ...,
        run_as_non_root: typing.Optional[bool] = ...,
        run_as_user: typing.Optional[int] = ...,
        se_linux_options: typing.Optional[kubernetes.client.V1SELinuxOptions] = ...,
        windows_options: typing.Optional[
            kubernetes.client.V1WindowsSecurityContextOptions
        ] = ...
    ) -> None: ...