from kubernetes.client.models.admissionregistration_v1_service_reference import \
    AdmissionregistrationV1ServiceReference
from kubernetes.client.models.admissionregistration_v1_webhook_client_config import \
    AdmissionregistrationV1WebhookClientConfig
from kubernetes.client.models.admissionregistration_v1beta1_service_reference import \
    AdmissionregistrationV1beta1ServiceReference
from kubernetes.client.models.admissionregistration_v1beta1_webhook_client_config import \
    AdmissionregistrationV1beta1WebhookClientConfig
from kubernetes.client.models.apiextensions_v1_service_reference import \
    ApiextensionsV1ServiceReference
from kubernetes.client.models.apiextensions_v1_webhook_client_config import \
    ApiextensionsV1WebhookClientConfig
from kubernetes.client.models.apiextensions_v1beta1_service_reference import \
    ApiextensionsV1beta1ServiceReference
from kubernetes.client.models.apiextensions_v1beta1_webhook_client_config import \
    ApiextensionsV1beta1WebhookClientConfig
from kubernetes.client.models.apiregistration_v1_service_reference import \
    ApiregistrationV1ServiceReference
from kubernetes.client.models.apiregistration_v1beta1_service_reference import \
    ApiregistrationV1beta1ServiceReference
from kubernetes.client.models.apps_v1beta1_deployment import \
    AppsV1beta1Deployment
from kubernetes.client.models.apps_v1beta1_deployment_condition import \
    AppsV1beta1DeploymentCondition
from kubernetes.client.models.apps_v1beta1_deployment_list import \
    AppsV1beta1DeploymentList
from kubernetes.client.models.apps_v1beta1_deployment_rollback import \
    AppsV1beta1DeploymentRollback
from kubernetes.client.models.apps_v1beta1_deployment_spec import \
    AppsV1beta1DeploymentSpec
from kubernetes.client.models.apps_v1beta1_deployment_status import \
    AppsV1beta1DeploymentStatus
from kubernetes.client.models.apps_v1beta1_deployment_strategy import \
    AppsV1beta1DeploymentStrategy
from kubernetes.client.models.apps_v1beta1_rollback_config import \
    AppsV1beta1RollbackConfig
from kubernetes.client.models.apps_v1beta1_rolling_update_deployment import \
    AppsV1beta1RollingUpdateDeployment
from kubernetes.client.models.apps_v1beta1_scale import AppsV1beta1Scale
from kubernetes.client.models.apps_v1beta1_scale_spec import \
    AppsV1beta1ScaleSpec
from kubernetes.client.models.apps_v1beta1_scale_status import \
    AppsV1beta1ScaleStatus
from kubernetes.client.models.extensions_v1beta1_allowed_csi_driver import \
    ExtensionsV1beta1AllowedCSIDriver
from kubernetes.client.models.extensions_v1beta1_allowed_flex_volume import \
    ExtensionsV1beta1AllowedFlexVolume
from kubernetes.client.models.extensions_v1beta1_allowed_host_path import \
    ExtensionsV1beta1AllowedHostPath
from kubernetes.client.models.extensions_v1beta1_deployment import \
    ExtensionsV1beta1Deployment
from kubernetes.client.models.extensions_v1beta1_deployment_condition import \
    ExtensionsV1beta1DeploymentCondition
from kubernetes.client.models.extensions_v1beta1_deployment_list import \
    ExtensionsV1beta1DeploymentList
from kubernetes.client.models.extensions_v1beta1_deployment_rollback import \
    ExtensionsV1beta1DeploymentRollback
from kubernetes.client.models.extensions_v1beta1_deployment_spec import \
    ExtensionsV1beta1DeploymentSpec
from kubernetes.client.models.extensions_v1beta1_deployment_status import \
    ExtensionsV1beta1DeploymentStatus
from kubernetes.client.models.extensions_v1beta1_deployment_strategy import \
    ExtensionsV1beta1DeploymentStrategy
from kubernetes.client.models.extensions_v1beta1_fs_group_strategy_options import \
    ExtensionsV1beta1FSGroupStrategyOptions
from kubernetes.client.models.extensions_v1beta1_host_port_range import \
    ExtensionsV1beta1HostPortRange
from kubernetes.client.models.extensions_v1beta1_http_ingress_path import \
    ExtensionsV1beta1HTTPIngressPath
from kubernetes.client.models.extensions_v1beta1_http_ingress_rule_value import \
    ExtensionsV1beta1HTTPIngressRuleValue
from kubernetes.client.models.extensions_v1beta1_id_range import \
    ExtensionsV1beta1IDRange
from kubernetes.client.models.extensions_v1beta1_ingress import \
    ExtensionsV1beta1Ingress
from kubernetes.client.models.extensions_v1beta1_ingress_backend import \
    ExtensionsV1beta1IngressBackend
from kubernetes.client.models.extensions_v1beta1_ingress_list import \
    ExtensionsV1beta1IngressList
from kubernetes.client.models.extensions_v1beta1_ingress_rule import \
    ExtensionsV1beta1IngressRule
from kubernetes.client.models.extensions_v1beta1_ingress_spec import \
    ExtensionsV1beta1IngressSpec
from kubernetes.client.models.extensions_v1beta1_ingress_status import \
    ExtensionsV1beta1IngressStatus
from kubernetes.client.models.extensions_v1beta1_ingress_tls import \
    ExtensionsV1beta1IngressTLS
from kubernetes.client.models.extensions_v1beta1_pod_security_policy import \
    ExtensionsV1beta1PodSecurityPolicy
from kubernetes.client.models.extensions_v1beta1_pod_security_policy_list import \
    ExtensionsV1beta1PodSecurityPolicyList
from kubernetes.client.models.extensions_v1beta1_pod_security_policy_spec import \
    ExtensionsV1beta1PodSecurityPolicySpec
from kubernetes.client.models.extensions_v1beta1_rollback_config import \
    ExtensionsV1beta1RollbackConfig
from kubernetes.client.models.extensions_v1beta1_rolling_update_deployment import \
    ExtensionsV1beta1RollingUpdateDeployment
from kubernetes.client.models.extensions_v1beta1_run_as_group_strategy_options import \
    ExtensionsV1beta1RunAsGroupStrategyOptions
from kubernetes.client.models.extensions_v1beta1_run_as_user_strategy_options import \
    ExtensionsV1beta1RunAsUserStrategyOptions
from kubernetes.client.models.extensions_v1beta1_runtime_class_strategy_options import \
    ExtensionsV1beta1RuntimeClassStrategyOptions
from kubernetes.client.models.extensions_v1beta1_scale import \
    ExtensionsV1beta1Scale
from kubernetes.client.models.extensions_v1beta1_scale_spec import \
    ExtensionsV1beta1ScaleSpec
from kubernetes.client.models.extensions_v1beta1_scale_status import \
    ExtensionsV1beta1ScaleStatus
from kubernetes.client.models.extensions_v1beta1_se_linux_strategy_options import \
    ExtensionsV1beta1SELinuxStrategyOptions
from kubernetes.client.models.extensions_v1beta1_supplemental_groups_strategy_options import \
    ExtensionsV1beta1SupplementalGroupsStrategyOptions
from kubernetes.client.models.flowcontrol_v1alpha1_subject import \
    FlowcontrolV1alpha1Subject
from kubernetes.client.models.networking_v1beta1_http_ingress_path import \
    NetworkingV1beta1HTTPIngressPath
from kubernetes.client.models.networking_v1beta1_http_ingress_rule_value import \
    NetworkingV1beta1HTTPIngressRuleValue
from kubernetes.client.models.networking_v1beta1_ingress import \
    NetworkingV1beta1Ingress
from kubernetes.client.models.networking_v1beta1_ingress_backend import \
    NetworkingV1beta1IngressBackend
from kubernetes.client.models.networking_v1beta1_ingress_list import \
    NetworkingV1beta1IngressList
from kubernetes.client.models.networking_v1beta1_ingress_rule import \
    NetworkingV1beta1IngressRule
from kubernetes.client.models.networking_v1beta1_ingress_spec import \
    NetworkingV1beta1IngressSpec
from kubernetes.client.models.networking_v1beta1_ingress_status import \
    NetworkingV1beta1IngressStatus
from kubernetes.client.models.networking_v1beta1_ingress_tls import \
    NetworkingV1beta1IngressTLS
from kubernetes.client.models.policy_v1beta1_allowed_csi_driver import \
    PolicyV1beta1AllowedCSIDriver
from kubernetes.client.models.policy_v1beta1_allowed_flex_volume import \
    PolicyV1beta1AllowedFlexVolume
from kubernetes.client.models.policy_v1beta1_allowed_host_path import \
    PolicyV1beta1AllowedHostPath
from kubernetes.client.models.policy_v1beta1_fs_group_strategy_options import \
    PolicyV1beta1FSGroupStrategyOptions
from kubernetes.client.models.policy_v1beta1_host_port_range import \
    PolicyV1beta1HostPortRange
from kubernetes.client.models.policy_v1beta1_id_range import \
    PolicyV1beta1IDRange
from kubernetes.client.models.policy_v1beta1_pod_security_policy import \
    PolicyV1beta1PodSecurityPolicy
from kubernetes.client.models.policy_v1beta1_pod_security_policy_list import \
    PolicyV1beta1PodSecurityPolicyList
from kubernetes.client.models.policy_v1beta1_pod_security_policy_spec import \
    PolicyV1beta1PodSecurityPolicySpec
from kubernetes.client.models.policy_v1beta1_run_as_group_strategy_options import \
    PolicyV1beta1RunAsGroupStrategyOptions
from kubernetes.client.models.policy_v1beta1_run_as_user_strategy_options import \
    PolicyV1beta1RunAsUserStrategyOptions
from kubernetes.client.models.policy_v1beta1_runtime_class_strategy_options import \
    PolicyV1beta1RuntimeClassStrategyOptions
from kubernetes.client.models.policy_v1beta1_se_linux_strategy_options import \
    PolicyV1beta1SELinuxStrategyOptions
from kubernetes.client.models.policy_v1beta1_supplemental_groups_strategy_options import \
    PolicyV1beta1SupplementalGroupsStrategyOptions
from kubernetes.client.models.rbac_v1alpha1_subject import RbacV1alpha1Subject
from kubernetes.client.models.v1_affinity import V1Affinity
from kubernetes.client.models.v1_aggregation_rule import V1AggregationRule
from kubernetes.client.models.v1_api_group import V1APIGroup
from kubernetes.client.models.v1_api_group_list import V1APIGroupList
from kubernetes.client.models.v1_api_resource import V1APIResource
from kubernetes.client.models.v1_api_resource_list import V1APIResourceList
from kubernetes.client.models.v1_api_service import V1APIService
from kubernetes.client.models.v1_api_service_condition import \
    V1APIServiceCondition
from kubernetes.client.models.v1_api_service_list import V1APIServiceList
from kubernetes.client.models.v1_api_service_spec import V1APIServiceSpec
from kubernetes.client.models.v1_api_service_status import V1APIServiceStatus
from kubernetes.client.models.v1_api_versions import V1APIVersions
from kubernetes.client.models.v1_attached_volume import V1AttachedVolume
from kubernetes.client.models.v1_aws_elastic_block_store_volume_source import \
    V1AWSElasticBlockStoreVolumeSource
from kubernetes.client.models.v1_azure_disk_volume_source import \
    V1AzureDiskVolumeSource
from kubernetes.client.models.v1_azure_file_persistent_volume_source import \
    V1AzureFilePersistentVolumeSource
from kubernetes.client.models.v1_azure_file_volume_source import \
    V1AzureFileVolumeSource
from kubernetes.client.models.v1_binding import V1Binding
from kubernetes.client.models.v1_bound_object_reference import \
    V1BoundObjectReference
from kubernetes.client.models.v1_capabilities import V1Capabilities
from kubernetes.client.models.v1_ceph_fs_persistent_volume_source import \
    V1CephFSPersistentVolumeSource
from kubernetes.client.models.v1_ceph_fs_volume_source import \
    V1CephFSVolumeSource
from kubernetes.client.models.v1_cinder_persistent_volume_source import \
    V1CinderPersistentVolumeSource
from kubernetes.client.models.v1_cinder_volume_source import \
    V1CinderVolumeSource
from kubernetes.client.models.v1_client_ip_config import V1ClientIPConfig
from kubernetes.client.models.v1_cluster_role import V1ClusterRole
from kubernetes.client.models.v1_cluster_role_binding import \
    V1ClusterRoleBinding
from kubernetes.client.models.v1_cluster_role_binding_list import \
    V1ClusterRoleBindingList
from kubernetes.client.models.v1_cluster_role_list import V1ClusterRoleList
from kubernetes.client.models.v1_component_condition import \
    V1ComponentCondition
from kubernetes.client.models.v1_component_status import V1ComponentStatus
from kubernetes.client.models.v1_component_status_list import \
    V1ComponentStatusList
from kubernetes.client.models.v1_config_map import V1ConfigMap
from kubernetes.client.models.v1_config_map_env_source import \
    V1ConfigMapEnvSource
from kubernetes.client.models.v1_config_map_key_selector import \
    V1ConfigMapKeySelector
from kubernetes.client.models.v1_config_map_list import V1ConfigMapList
from kubernetes.client.models.v1_config_map_node_config_source import \
    V1ConfigMapNodeConfigSource
from kubernetes.client.models.v1_config_map_projection import \
    V1ConfigMapProjection
from kubernetes.client.models.v1_config_map_volume_source import \
    V1ConfigMapVolumeSource
from kubernetes.client.models.v1_container import V1Container
from kubernetes.client.models.v1_container_image import V1ContainerImage
from kubernetes.client.models.v1_container_port import V1ContainerPort
from kubernetes.client.models.v1_container_state import V1ContainerState
from kubernetes.client.models.v1_container_state_running import \
    V1ContainerStateRunning
from kubernetes.client.models.v1_container_state_terminated import \
    V1ContainerStateTerminated
from kubernetes.client.models.v1_container_state_waiting import \
    V1ContainerStateWaiting
from kubernetes.client.models.v1_container_status import V1ContainerStatus
from kubernetes.client.models.v1_controller_revision import \
    V1ControllerRevision
from kubernetes.client.models.v1_controller_revision_list import \
    V1ControllerRevisionList
from kubernetes.client.models.v1_cross_version_object_reference import \
    V1CrossVersionObjectReference
from kubernetes.client.models.v1_csi_node import V1CSINode
from kubernetes.client.models.v1_csi_node_driver import V1CSINodeDriver
from kubernetes.client.models.v1_csi_node_list import V1CSINodeList
from kubernetes.client.models.v1_csi_node_spec import V1CSINodeSpec
from kubernetes.client.models.v1_csi_persistent_volume_source import \
    V1CSIPersistentVolumeSource
from kubernetes.client.models.v1_csi_volume_source import V1CSIVolumeSource
from kubernetes.client.models.v1_custom_resource_column_definition import \
    V1CustomResourceColumnDefinition
from kubernetes.client.models.v1_custom_resource_conversion import \
    V1CustomResourceConversion
from kubernetes.client.models.v1_custom_resource_definition import \
    V1CustomResourceDefinition
from kubernetes.client.models.v1_custom_resource_definition_condition import \
    V1CustomResourceDefinitionCondition
from kubernetes.client.models.v1_custom_resource_definition_list import \
    V1CustomResourceDefinitionList
from kubernetes.client.models.v1_custom_resource_definition_names import \
    V1CustomResourceDefinitionNames
from kubernetes.client.models.v1_custom_resource_definition_spec import \
    V1CustomResourceDefinitionSpec
from kubernetes.client.models.v1_custom_resource_definition_status import \
    V1CustomResourceDefinitionStatus
from kubernetes.client.models.v1_custom_resource_definition_version import \
    V1CustomResourceDefinitionVersion
from kubernetes.client.models.v1_custom_resource_subresource_scale import \
    V1CustomResourceSubresourceScale
from kubernetes.client.models.v1_custom_resource_subresources import \
    V1CustomResourceSubresources
from kubernetes.client.models.v1_custom_resource_validation import \
    V1CustomResourceValidation
from kubernetes.client.models.v1_daemon_endpoint import V1DaemonEndpoint
from kubernetes.client.models.v1_daemon_set import V1DaemonSet
from kubernetes.client.models.v1_daemon_set_condition import \
    V1DaemonSetCondition
from kubernetes.client.models.v1_daemon_set_list import V1DaemonSetList
from kubernetes.client.models.v1_daemon_set_spec import V1DaemonSetSpec
from kubernetes.client.models.v1_daemon_set_status import V1DaemonSetStatus
from kubernetes.client.models.v1_daemon_set_update_strategy import \
    V1DaemonSetUpdateStrategy
from kubernetes.client.models.v1_delete_options import V1DeleteOptions
from kubernetes.client.models.v1_deployment import V1Deployment
from kubernetes.client.models.v1_deployment_condition import \
    V1DeploymentCondition
from kubernetes.client.models.v1_deployment_list import V1DeploymentList
from kubernetes.client.models.v1_deployment_spec import V1DeploymentSpec
from kubernetes.client.models.v1_deployment_status import V1DeploymentStatus
from kubernetes.client.models.v1_deployment_strategy import \
    V1DeploymentStrategy
from kubernetes.client.models.v1_downward_api_projection import \
    V1DownwardAPIProjection
from kubernetes.client.models.v1_downward_api_volume_file import \
    V1DownwardAPIVolumeFile
from kubernetes.client.models.v1_downward_api_volume_source import \
    V1DownwardAPIVolumeSource
from kubernetes.client.models.v1_empty_dir_volume_source import \
    V1EmptyDirVolumeSource
from kubernetes.client.models.v1_endpoint_address import V1EndpointAddress
from kubernetes.client.models.v1_endpoint_port import V1EndpointPort
from kubernetes.client.models.v1_endpoint_subset import V1EndpointSubset
from kubernetes.client.models.v1_endpoints import V1Endpoints
from kubernetes.client.models.v1_endpoints_list import V1EndpointsList
from kubernetes.client.models.v1_env_from_source import V1EnvFromSource
from kubernetes.client.models.v1_env_var import V1EnvVar
from kubernetes.client.models.v1_env_var_source import V1EnvVarSource
from kubernetes.client.models.v1_ephemeral_container import \
    V1EphemeralContainer
from kubernetes.client.models.v1_event import V1Event
from kubernetes.client.models.v1_event_list import V1EventList
from kubernetes.client.models.v1_event_series import V1EventSeries
from kubernetes.client.models.v1_event_source import V1EventSource
from kubernetes.client.models.v1_exec_action import V1ExecAction
from kubernetes.client.models.v1_external_documentation import \
    V1ExternalDocumentation
from kubernetes.client.models.v1_fc_volume_source import V1FCVolumeSource
from kubernetes.client.models.v1_flex_persistent_volume_source import \
    V1FlexPersistentVolumeSource
from kubernetes.client.models.v1_flex_volume_source import V1FlexVolumeSource
from kubernetes.client.models.v1_flocker_volume_source import \
    V1FlockerVolumeSource
from kubernetes.client.models.v1_gce_persistent_disk_volume_source import \
    V1GCEPersistentDiskVolumeSource
from kubernetes.client.models.v1_git_repo_volume_source import \
    V1GitRepoVolumeSource
from kubernetes.client.models.v1_glusterfs_persistent_volume_source import \
    V1GlusterfsPersistentVolumeSource
from kubernetes.client.models.v1_glusterfs_volume_source import \
    V1GlusterfsVolumeSource
from kubernetes.client.models.v1_group_version_for_discovery import \
    V1GroupVersionForDiscovery
from kubernetes.client.models.v1_handler import V1Handler
from kubernetes.client.models.v1_horizontal_pod_autoscaler import \
    V1HorizontalPodAutoscaler
from kubernetes.client.models.v1_horizontal_pod_autoscaler_list import \
    V1HorizontalPodAutoscalerList
from kubernetes.client.models.v1_horizontal_pod_autoscaler_spec import \
    V1HorizontalPodAutoscalerSpec
from kubernetes.client.models.v1_horizontal_pod_autoscaler_status import \
    V1HorizontalPodAutoscalerStatus
from kubernetes.client.models.v1_host_alias import V1HostAlias
from kubernetes.client.models.v1_host_path_volume_source import \
    V1HostPathVolumeSource
from kubernetes.client.models.v1_http_get_action import V1HTTPGetAction
from kubernetes.client.models.v1_http_header import V1HTTPHeader
from kubernetes.client.models.v1_ip_block import V1IPBlock
from kubernetes.client.models.v1_iscsi_persistent_volume_source import \
    V1ISCSIPersistentVolumeSource
from kubernetes.client.models.v1_iscsi_volume_source import V1ISCSIVolumeSource
from kubernetes.client.models.v1_job import V1Job
from kubernetes.client.models.v1_job_condition import V1JobCondition
from kubernetes.client.models.v1_job_list import V1JobList
from kubernetes.client.models.v1_job_spec import V1JobSpec
from kubernetes.client.models.v1_job_status import V1JobStatus
from kubernetes.client.models.v1_json_schema_props import V1JSONSchemaProps
from kubernetes.client.models.v1_key_to_path import V1KeyToPath
from kubernetes.client.models.v1_label_selector import V1LabelSelector
from kubernetes.client.models.v1_label_selector_requirement import \
    V1LabelSelectorRequirement
from kubernetes.client.models.v1_lease import V1Lease
from kubernetes.client.models.v1_lease_list import V1LeaseList
from kubernetes.client.models.v1_lease_spec import V1LeaseSpec
from kubernetes.client.models.v1_lifecycle import V1Lifecycle
from kubernetes.client.models.v1_limit_range import V1LimitRange
from kubernetes.client.models.v1_limit_range_item import V1LimitRangeItem
from kubernetes.client.models.v1_limit_range_list import V1LimitRangeList
from kubernetes.client.models.v1_limit_range_spec import V1LimitRangeSpec
from kubernetes.client.models.v1_list_meta import V1ListMeta
from kubernetes.client.models.v1_load_balancer_ingress import \
    V1LoadBalancerIngress
from kubernetes.client.models.v1_load_balancer_status import \
    V1LoadBalancerStatus
from kubernetes.client.models.v1_local_object_reference import \
    V1LocalObjectReference
from kubernetes.client.models.v1_local_subject_access_review import \
    V1LocalSubjectAccessReview
from kubernetes.client.models.v1_local_volume_source import V1LocalVolumeSource
from kubernetes.client.models.v1_managed_fields_entry import \
    V1ManagedFieldsEntry
from kubernetes.client.models.v1_mutating_webhook import V1MutatingWebhook
from kubernetes.client.models.v1_mutating_webhook_configuration import \
    V1MutatingWebhookConfiguration
from kubernetes.client.models.v1_mutating_webhook_configuration_list import \
    V1MutatingWebhookConfigurationList
from kubernetes.client.models.v1_namespace import V1Namespace
from kubernetes.client.models.v1_namespace_condition import \
    V1NamespaceCondition
from kubernetes.client.models.v1_namespace_list import V1NamespaceList
from kubernetes.client.models.v1_namespace_spec import V1NamespaceSpec
from kubernetes.client.models.v1_namespace_status import V1NamespaceStatus
from kubernetes.client.models.v1_network_policy import V1NetworkPolicy
from kubernetes.client.models.v1_network_policy_egress_rule import \
    V1NetworkPolicyEgressRule
from kubernetes.client.models.v1_network_policy_ingress_rule import \
    V1NetworkPolicyIngressRule
from kubernetes.client.models.v1_network_policy_list import V1NetworkPolicyList
from kubernetes.client.models.v1_network_policy_peer import V1NetworkPolicyPeer
from kubernetes.client.models.v1_network_policy_port import V1NetworkPolicyPort
from kubernetes.client.models.v1_network_policy_spec import V1NetworkPolicySpec
from kubernetes.client.models.v1_nfs_volume_source import V1NFSVolumeSource
from kubernetes.client.models.v1_node import V1Node
from kubernetes.client.models.v1_node_address import V1NodeAddress
from kubernetes.client.models.v1_node_affinity import V1NodeAffinity
from kubernetes.client.models.v1_node_condition import V1NodeCondition
from kubernetes.client.models.v1_node_config_source import V1NodeConfigSource
from kubernetes.client.models.v1_node_config_status import V1NodeConfigStatus
from kubernetes.client.models.v1_node_daemon_endpoints import \
    V1NodeDaemonEndpoints
from kubernetes.client.models.v1_node_list import V1NodeList
from kubernetes.client.models.v1_node_selector import V1NodeSelector
from kubernetes.client.models.v1_node_selector_requirement import \
    V1NodeSelectorRequirement
from kubernetes.client.models.v1_node_selector_term import V1NodeSelectorTerm
from kubernetes.client.models.v1_node_spec import V1NodeSpec
from kubernetes.client.models.v1_node_status import V1NodeStatus
from kubernetes.client.models.v1_node_system_info import V1NodeSystemInfo
from kubernetes.client.models.v1_non_resource_attributes import \
    V1NonResourceAttributes
from kubernetes.client.models.v1_non_resource_rule import V1NonResourceRule
from kubernetes.client.models.v1_object_field_selector import \
    V1ObjectFieldSelector
from kubernetes.client.models.v1_object_meta import V1ObjectMeta
from kubernetes.client.models.v1_object_reference import V1ObjectReference
from kubernetes.client.models.v1_owner_reference import V1OwnerReference
from kubernetes.client.models.v1_persistent_volume import V1PersistentVolume
from kubernetes.client.models.v1_persistent_volume_claim import \
    V1PersistentVolumeClaim
from kubernetes.client.models.v1_persistent_volume_claim_condition import \
    V1PersistentVolumeClaimCondition
from kubernetes.client.models.v1_persistent_volume_claim_list import \
    V1PersistentVolumeClaimList
from kubernetes.client.models.v1_persistent_volume_claim_spec import \
    V1PersistentVolumeClaimSpec
from kubernetes.client.models.v1_persistent_volume_claim_status import \
    V1PersistentVolumeClaimStatus
from kubernetes.client.models.v1_persistent_volume_claim_volume_source import \
    V1PersistentVolumeClaimVolumeSource
from kubernetes.client.models.v1_persistent_volume_list import \
    V1PersistentVolumeList
from kubernetes.client.models.v1_persistent_volume_spec import \
    V1PersistentVolumeSpec
from kubernetes.client.models.v1_persistent_volume_status import \
    V1PersistentVolumeStatus
from kubernetes.client.models.v1_photon_persistent_disk_volume_source import \
    V1PhotonPersistentDiskVolumeSource
from kubernetes.client.models.v1_pod import V1Pod
from kubernetes.client.models.v1_pod_affinity import V1PodAffinity
from kubernetes.client.models.v1_pod_affinity_term import V1PodAffinityTerm
from kubernetes.client.models.v1_pod_anti_affinity import V1PodAntiAffinity
from kubernetes.client.models.v1_pod_condition import V1PodCondition
from kubernetes.client.models.v1_pod_dns_config import V1PodDNSConfig
from kubernetes.client.models.v1_pod_dns_config_option import \
    V1PodDNSConfigOption
from kubernetes.client.models.v1_pod_ip import V1PodIP
from kubernetes.client.models.v1_pod_list import V1PodList
from kubernetes.client.models.v1_pod_readiness_gate import V1PodReadinessGate
from kubernetes.client.models.v1_pod_security_context import \
    V1PodSecurityContext
from kubernetes.client.models.v1_pod_spec import V1PodSpec
from kubernetes.client.models.v1_pod_status import V1PodStatus
from kubernetes.client.models.v1_pod_template import V1PodTemplate
from kubernetes.client.models.v1_pod_template_list import V1PodTemplateList
from kubernetes.client.models.v1_pod_template_spec import V1PodTemplateSpec
from kubernetes.client.models.v1_policy_rule import V1PolicyRule
from kubernetes.client.models.v1_portworx_volume_source import \
    V1PortworxVolumeSource
from kubernetes.client.models.v1_preconditions import V1Preconditions
from kubernetes.client.models.v1_preferred_scheduling_term import \
    V1PreferredSchedulingTerm
from kubernetes.client.models.v1_priority_class import V1PriorityClass
from kubernetes.client.models.v1_priority_class_list import V1PriorityClassList
from kubernetes.client.models.v1_probe import V1Probe
from kubernetes.client.models.v1_projected_volume_source import \
    V1ProjectedVolumeSource
from kubernetes.client.models.v1_quobyte_volume_source import \
    V1QuobyteVolumeSource
from kubernetes.client.models.v1_rbd_persistent_volume_source import \
    V1RBDPersistentVolumeSource
from kubernetes.client.models.v1_rbd_volume_source import V1RBDVolumeSource
from kubernetes.client.models.v1_replica_set import V1ReplicaSet
from kubernetes.client.models.v1_replica_set_condition import \
    V1ReplicaSetCondition
from kubernetes.client.models.v1_replica_set_list import V1ReplicaSetList
from kubernetes.client.models.v1_replica_set_spec import V1ReplicaSetSpec
from kubernetes.client.models.v1_replica_set_status import V1ReplicaSetStatus
from kubernetes.client.models.v1_replication_controller import \
    V1ReplicationController
from kubernetes.client.models.v1_replication_controller_condition import \
    V1ReplicationControllerCondition
from kubernetes.client.models.v1_replication_controller_list import \
    V1ReplicationControllerList
from kubernetes.client.models.v1_replication_controller_spec import \
    V1ReplicationControllerSpec
from kubernetes.client.models.v1_replication_controller_status import \
    V1ReplicationControllerStatus
from kubernetes.client.models.v1_resource_attributes import \
    V1ResourceAttributes
from kubernetes.client.models.v1_resource_field_selector import \
    V1ResourceFieldSelector
from kubernetes.client.models.v1_resource_quota import V1ResourceQuota
from kubernetes.client.models.v1_resource_quota_list import V1ResourceQuotaList
from kubernetes.client.models.v1_resource_quota_spec import V1ResourceQuotaSpec
from kubernetes.client.models.v1_resource_quota_status import \
    V1ResourceQuotaStatus
from kubernetes.client.models.v1_resource_requirements import \
    V1ResourceRequirements
from kubernetes.client.models.v1_resource_rule import V1ResourceRule
from kubernetes.client.models.v1_role import V1Role
from kubernetes.client.models.v1_role_binding import V1RoleBinding
from kubernetes.client.models.v1_role_binding_list import V1RoleBindingList
from kubernetes.client.models.v1_role_list import V1RoleList
from kubernetes.client.models.v1_role_ref import V1RoleRef
from kubernetes.client.models.v1_rolling_update_daemon_set import \
    V1RollingUpdateDaemonSet
from kubernetes.client.models.v1_rolling_update_deployment import \
    V1RollingUpdateDeployment
from kubernetes.client.models.v1_rolling_update_stateful_set_strategy import \
    V1RollingUpdateStatefulSetStrategy
from kubernetes.client.models.v1_rule_with_operations import \
    V1RuleWithOperations
from kubernetes.client.models.v1_scale import V1Scale
from kubernetes.client.models.v1_scale_io_persistent_volume_source import \
    V1ScaleIOPersistentVolumeSource
from kubernetes.client.models.v1_scale_io_volume_source import \
    V1ScaleIOVolumeSource
from kubernetes.client.models.v1_scale_spec import V1ScaleSpec
from kubernetes.client.models.v1_scale_status import V1ScaleStatus
from kubernetes.client.models.v1_scope_selector import V1ScopeSelector
from kubernetes.client.models.v1_scoped_resource_selector_requirement import \
    V1ScopedResourceSelectorRequirement
from kubernetes.client.models.v1_se_linux_options import V1SELinuxOptions
from kubernetes.client.models.v1_secret import V1Secret
from kubernetes.client.models.v1_secret_env_source import V1SecretEnvSource
from kubernetes.client.models.v1_secret_key_selector import V1SecretKeySelector
from kubernetes.client.models.v1_secret_list import V1SecretList
from kubernetes.client.models.v1_secret_projection import V1SecretProjection
from kubernetes.client.models.v1_secret_reference import V1SecretReference
from kubernetes.client.models.v1_secret_volume_source import \
    V1SecretVolumeSource
from kubernetes.client.models.v1_security_context import V1SecurityContext
from kubernetes.client.models.v1_self_subject_access_review import \
    V1SelfSubjectAccessReview
from kubernetes.client.models.v1_self_subject_access_review_spec import \
    V1SelfSubjectAccessReviewSpec
from kubernetes.client.models.v1_self_subject_rules_review import \
    V1SelfSubjectRulesReview
from kubernetes.client.models.v1_self_subject_rules_review_spec import \
    V1SelfSubjectRulesReviewSpec
from kubernetes.client.models.v1_server_address_by_client_cidr import \
    V1ServerAddressByClientCIDR
from kubernetes.client.models.v1_service import V1Service
from kubernetes.client.models.v1_service_account import V1ServiceAccount
from kubernetes.client.models.v1_service_account_list import \
    V1ServiceAccountList
from kubernetes.client.models.v1_service_account_token_projection import \
    V1ServiceAccountTokenProjection
from kubernetes.client.models.v1_service_list import V1ServiceList
from kubernetes.client.models.v1_service_port import V1ServicePort
from kubernetes.client.models.v1_service_spec import V1ServiceSpec
from kubernetes.client.models.v1_service_status import V1ServiceStatus
from kubernetes.client.models.v1_session_affinity_config import \
    V1SessionAffinityConfig
from kubernetes.client.models.v1_stateful_set import V1StatefulSet
from kubernetes.client.models.v1_stateful_set_condition import \
    V1StatefulSetCondition
from kubernetes.client.models.v1_stateful_set_list import V1StatefulSetList
from kubernetes.client.models.v1_stateful_set_spec import V1StatefulSetSpec
from kubernetes.client.models.v1_stateful_set_status import V1StatefulSetStatus
from kubernetes.client.models.v1_stateful_set_update_strategy import \
    V1StatefulSetUpdateStrategy
from kubernetes.client.models.v1_status import V1Status
from kubernetes.client.models.v1_status_cause import V1StatusCause
from kubernetes.client.models.v1_status_details import V1StatusDetails
from kubernetes.client.models.v1_storage_class import V1StorageClass
from kubernetes.client.models.v1_storage_class_list import V1StorageClassList
from kubernetes.client.models.v1_storage_os_persistent_volume_source import \
    V1StorageOSPersistentVolumeSource
from kubernetes.client.models.v1_storage_os_volume_source import \
    V1StorageOSVolumeSource
from kubernetes.client.models.v1_subject import V1Subject
from kubernetes.client.models.v1_subject_access_review import \
    V1SubjectAccessReview
from kubernetes.client.models.v1_subject_access_review_spec import \
    V1SubjectAccessReviewSpec
from kubernetes.client.models.v1_subject_access_review_status import \
    V1SubjectAccessReviewStatus
from kubernetes.client.models.v1_subject_rules_review_status import \
    V1SubjectRulesReviewStatus
from kubernetes.client.models.v1_sysctl import V1Sysctl
from kubernetes.client.models.v1_taint import V1Taint
from kubernetes.client.models.v1_tcp_socket_action import V1TCPSocketAction
from kubernetes.client.models.v1_token_request import V1TokenRequest
from kubernetes.client.models.v1_token_request_spec import V1TokenRequestSpec
from kubernetes.client.models.v1_token_request_status import \
    V1TokenRequestStatus
from kubernetes.client.models.v1_token_review import V1TokenReview
from kubernetes.client.models.v1_token_review_spec import V1TokenReviewSpec
from kubernetes.client.models.v1_token_review_status import V1TokenReviewStatus
from kubernetes.client.models.v1_toleration import V1Toleration
from kubernetes.client.models.v1_topology_selector_label_requirement import \
    V1TopologySelectorLabelRequirement
from kubernetes.client.models.v1_topology_selector_term import \
    V1TopologySelectorTerm
from kubernetes.client.models.v1_topology_spread_constraint import \
    V1TopologySpreadConstraint
from kubernetes.client.models.v1_typed_local_object_reference import \
    V1TypedLocalObjectReference
from kubernetes.client.models.v1_user_info import V1UserInfo
from kubernetes.client.models.v1_validating_webhook import V1ValidatingWebhook
from kubernetes.client.models.v1_validating_webhook_configuration import \
    V1ValidatingWebhookConfiguration
from kubernetes.client.models.v1_validating_webhook_configuration_list import \
    V1ValidatingWebhookConfigurationList
from kubernetes.client.models.v1_volume import V1Volume
from kubernetes.client.models.v1_volume_attachment import V1VolumeAttachment
from kubernetes.client.models.v1_volume_attachment_list import \
    V1VolumeAttachmentList
from kubernetes.client.models.v1_volume_attachment_source import \
    V1VolumeAttachmentSource
from kubernetes.client.models.v1_volume_attachment_spec import \
    V1VolumeAttachmentSpec
from kubernetes.client.models.v1_volume_attachment_status import \
    V1VolumeAttachmentStatus
from kubernetes.client.models.v1_volume_device import V1VolumeDevice
from kubernetes.client.models.v1_volume_error import V1VolumeError
from kubernetes.client.models.v1_volume_mount import V1VolumeMount
from kubernetes.client.models.v1_volume_node_affinity import \
    V1VolumeNodeAffinity
from kubernetes.client.models.v1_volume_node_resources import \
    V1VolumeNodeResources
from kubernetes.client.models.v1_volume_projection import V1VolumeProjection
from kubernetes.client.models.v1_vsphere_virtual_disk_volume_source import \
    V1VsphereVirtualDiskVolumeSource
from kubernetes.client.models.v1_watch_event import V1WatchEvent
from kubernetes.client.models.v1_webhook_conversion import V1WebhookConversion
from kubernetes.client.models.v1_weighted_pod_affinity_term import \
    V1WeightedPodAffinityTerm
from kubernetes.client.models.v1_windows_security_context_options import \
    V1WindowsSecurityContextOptions
from kubernetes.client.models.v1alpha1_aggregation_rule import \
    V1alpha1AggregationRule
from kubernetes.client.models.v1alpha1_audit_sink import V1alpha1AuditSink
from kubernetes.client.models.v1alpha1_audit_sink_list import \
    V1alpha1AuditSinkList
from kubernetes.client.models.v1alpha1_audit_sink_spec import \
    V1alpha1AuditSinkSpec
from kubernetes.client.models.v1alpha1_cluster_role import V1alpha1ClusterRole
from kubernetes.client.models.v1alpha1_cluster_role_binding import \
    V1alpha1ClusterRoleBinding
from kubernetes.client.models.v1alpha1_cluster_role_binding_list import \
    V1alpha1ClusterRoleBindingList
from kubernetes.client.models.v1alpha1_cluster_role_list import \
    V1alpha1ClusterRoleList
from kubernetes.client.models.v1alpha1_flow_distinguisher_method import \
    V1alpha1FlowDistinguisherMethod
from kubernetes.client.models.v1alpha1_flow_schema import V1alpha1FlowSchema
from kubernetes.client.models.v1alpha1_flow_schema_condition import \
    V1alpha1FlowSchemaCondition
from kubernetes.client.models.v1alpha1_flow_schema_list import \
    V1alpha1FlowSchemaList
from kubernetes.client.models.v1alpha1_flow_schema_spec import \
    V1alpha1FlowSchemaSpec
from kubernetes.client.models.v1alpha1_flow_schema_status import \
    V1alpha1FlowSchemaStatus
from kubernetes.client.models.v1alpha1_group_subject import \
    V1alpha1GroupSubject
from kubernetes.client.models.v1alpha1_limit_response import \
    V1alpha1LimitResponse
from kubernetes.client.models.v1alpha1_limited_priority_level_configuration import \
    V1alpha1LimitedPriorityLevelConfiguration
from kubernetes.client.models.v1alpha1_non_resource_policy_rule import \
    V1alpha1NonResourcePolicyRule
from kubernetes.client.models.v1alpha1_overhead import V1alpha1Overhead
from kubernetes.client.models.v1alpha1_pod_preset import V1alpha1PodPreset
from kubernetes.client.models.v1alpha1_pod_preset_list import \
    V1alpha1PodPresetList
from kubernetes.client.models.v1alpha1_pod_preset_spec import \
    V1alpha1PodPresetSpec
from kubernetes.client.models.v1alpha1_policy import V1alpha1Policy
from kubernetes.client.models.v1alpha1_policy_rule import V1alpha1PolicyRule
from kubernetes.client.models.v1alpha1_policy_rules_with_subjects import \
    V1alpha1PolicyRulesWithSubjects
from kubernetes.client.models.v1alpha1_priority_class import \
    V1alpha1PriorityClass
from kubernetes.client.models.v1alpha1_priority_class_list import \
    V1alpha1PriorityClassList
from kubernetes.client.models.v1alpha1_priority_level_configuration import \
    V1alpha1PriorityLevelConfiguration
from kubernetes.client.models.v1alpha1_priority_level_configuration_condition import \
    V1alpha1PriorityLevelConfigurationCondition
from kubernetes.client.models.v1alpha1_priority_level_configuration_list import \
    V1alpha1PriorityLevelConfigurationList
from kubernetes.client.models.v1alpha1_priority_level_configuration_reference import \
    V1alpha1PriorityLevelConfigurationReference
from kubernetes.client.models.v1alpha1_priority_level_configuration_spec import \
    V1alpha1PriorityLevelConfigurationSpec
from kubernetes.client.models.v1alpha1_priority_level_configuration_status import \
    V1alpha1PriorityLevelConfigurationStatus
from kubernetes.client.models.v1alpha1_queuing_configuration import \
    V1alpha1QueuingConfiguration
from kubernetes.client.models.v1alpha1_resource_policy_rule import \
    V1alpha1ResourcePolicyRule
from kubernetes.client.models.v1alpha1_role import V1alpha1Role
from kubernetes.client.models.v1alpha1_role_binding import V1alpha1RoleBinding
from kubernetes.client.models.v1alpha1_role_binding_list import \
    V1alpha1RoleBindingList
from kubernetes.client.models.v1alpha1_role_list import V1alpha1RoleList
from kubernetes.client.models.v1alpha1_role_ref import V1alpha1RoleRef
from kubernetes.client.models.v1alpha1_runtime_class import \
    V1alpha1RuntimeClass
from kubernetes.client.models.v1alpha1_runtime_class_list import \
    V1alpha1RuntimeClassList
from kubernetes.client.models.v1alpha1_runtime_class_spec import \
    V1alpha1RuntimeClassSpec
from kubernetes.client.models.v1alpha1_scheduling import V1alpha1Scheduling
from kubernetes.client.models.v1alpha1_service_account_subject import \
    V1alpha1ServiceAccountSubject
from kubernetes.client.models.v1alpha1_service_reference import \
    V1alpha1ServiceReference
from kubernetes.client.models.v1alpha1_user_subject import V1alpha1UserSubject
from kubernetes.client.models.v1alpha1_volume_attachment import \
    V1alpha1VolumeAttachment
from kubernetes.client.models.v1alpha1_volume_attachment_list import \
    V1alpha1VolumeAttachmentList
from kubernetes.client.models.v1alpha1_volume_attachment_source import \
    V1alpha1VolumeAttachmentSource
from kubernetes.client.models.v1alpha1_volume_attachment_spec import \
    V1alpha1VolumeAttachmentSpec
from kubernetes.client.models.v1alpha1_volume_attachment_status import \
    V1alpha1VolumeAttachmentStatus
from kubernetes.client.models.v1alpha1_volume_error import V1alpha1VolumeError
from kubernetes.client.models.v1alpha1_webhook import V1alpha1Webhook
from kubernetes.client.models.v1alpha1_webhook_client_config import \
    V1alpha1WebhookClientConfig
from kubernetes.client.models.v1alpha1_webhook_throttle_config import \
    V1alpha1WebhookThrottleConfig
from kubernetes.client.models.v1beta1_aggregation_rule import \
    V1beta1AggregationRule
from kubernetes.client.models.v1beta1_api_service import V1beta1APIService
from kubernetes.client.models.v1beta1_api_service_condition import \
    V1beta1APIServiceCondition
from kubernetes.client.models.v1beta1_api_service_list import \
    V1beta1APIServiceList
from kubernetes.client.models.v1beta1_api_service_spec import \
    V1beta1APIServiceSpec
from kubernetes.client.models.v1beta1_api_service_status import \
    V1beta1APIServiceStatus
from kubernetes.client.models.v1beta1_certificate_signing_request import \
    V1beta1CertificateSigningRequest
from kubernetes.client.models.v1beta1_certificate_signing_request_condition import \
    V1beta1CertificateSigningRequestCondition
from kubernetes.client.models.v1beta1_certificate_signing_request_list import \
    V1beta1CertificateSigningRequestList
from kubernetes.client.models.v1beta1_certificate_signing_request_spec import \
    V1beta1CertificateSigningRequestSpec
from kubernetes.client.models.v1beta1_certificate_signing_request_status import \
    V1beta1CertificateSigningRequestStatus
from kubernetes.client.models.v1beta1_cluster_role import V1beta1ClusterRole
from kubernetes.client.models.v1beta1_cluster_role_binding import \
    V1beta1ClusterRoleBinding
from kubernetes.client.models.v1beta1_cluster_role_binding_list import \
    V1beta1ClusterRoleBindingList
from kubernetes.client.models.v1beta1_cluster_role_list import \
    V1beta1ClusterRoleList
from kubernetes.client.models.v1beta1_controller_revision import \
    V1beta1ControllerRevision
from kubernetes.client.models.v1beta1_controller_revision_list import \
    V1beta1ControllerRevisionList
from kubernetes.client.models.v1beta1_cron_job import V1beta1CronJob
from kubernetes.client.models.v1beta1_cron_job_list import V1beta1CronJobList
from kubernetes.client.models.v1beta1_cron_job_spec import V1beta1CronJobSpec
from kubernetes.client.models.v1beta1_cron_job_status import \
    V1beta1CronJobStatus
from kubernetes.client.models.v1beta1_csi_driver import V1beta1CSIDriver
from kubernetes.client.models.v1beta1_csi_driver_list import \
    V1beta1CSIDriverList
from kubernetes.client.models.v1beta1_csi_driver_spec import \
    V1beta1CSIDriverSpec
from kubernetes.client.models.v1beta1_csi_node import V1beta1CSINode
from kubernetes.client.models.v1beta1_csi_node_driver import \
    V1beta1CSINodeDriver
from kubernetes.client.models.v1beta1_csi_node_list import V1beta1CSINodeList
from kubernetes.client.models.v1beta1_csi_node_spec import V1beta1CSINodeSpec
from kubernetes.client.models.v1beta1_custom_resource_column_definition import \
    V1beta1CustomResourceColumnDefinition
from kubernetes.client.models.v1beta1_custom_resource_conversion import \
    V1beta1CustomResourceConversion
from kubernetes.client.models.v1beta1_custom_resource_definition import \
    V1beta1CustomResourceDefinition
from kubernetes.client.models.v1beta1_custom_resource_definition_condition import \
    V1beta1CustomResourceDefinitionCondition
from kubernetes.client.models.v1beta1_custom_resource_definition_list import \
    V1beta1CustomResourceDefinitionList
from kubernetes.client.models.v1beta1_custom_resource_definition_names import \
    V1beta1CustomResourceDefinitionNames
from kubernetes.client.models.v1beta1_custom_resource_definition_spec import \
    V1beta1CustomResourceDefinitionSpec
from kubernetes.client.models.v1beta1_custom_resource_definition_status import \
    V1beta1CustomResourceDefinitionStatus
from kubernetes.client.models.v1beta1_custom_resource_definition_version import \
    V1beta1CustomResourceDefinitionVersion
from kubernetes.client.models.v1beta1_custom_resource_subresource_scale import \
    V1beta1CustomResourceSubresourceScale
from kubernetes.client.models.v1beta1_custom_resource_subresources import \
    V1beta1CustomResourceSubresources
from kubernetes.client.models.v1beta1_custom_resource_validation import \
    V1beta1CustomResourceValidation
from kubernetes.client.models.v1beta1_daemon_set import V1beta1DaemonSet
from kubernetes.client.models.v1beta1_daemon_set_condition import \
    V1beta1DaemonSetCondition
from kubernetes.client.models.v1beta1_daemon_set_list import \
    V1beta1DaemonSetList
from kubernetes.client.models.v1beta1_daemon_set_spec import \
    V1beta1DaemonSetSpec
from kubernetes.client.models.v1beta1_daemon_set_status import \
    V1beta1DaemonSetStatus
from kubernetes.client.models.v1beta1_daemon_set_update_strategy import \
    V1beta1DaemonSetUpdateStrategy
from kubernetes.client.models.v1beta1_endpoint import V1beta1Endpoint
from kubernetes.client.models.v1beta1_endpoint_conditions import \
    V1beta1EndpointConditions
from kubernetes.client.models.v1beta1_endpoint_port import V1beta1EndpointPort
from kubernetes.client.models.v1beta1_endpoint_slice import \
    V1beta1EndpointSlice
from kubernetes.client.models.v1beta1_endpoint_slice_list import \
    V1beta1EndpointSliceList
from kubernetes.client.models.v1beta1_event import V1beta1Event
from kubernetes.client.models.v1beta1_event_list import V1beta1EventList
from kubernetes.client.models.v1beta1_event_series import V1beta1EventSeries
from kubernetes.client.models.v1beta1_eviction import V1beta1Eviction
from kubernetes.client.models.v1beta1_external_documentation import \
    V1beta1ExternalDocumentation
from kubernetes.client.models.v1beta1_ip_block import V1beta1IPBlock
from kubernetes.client.models.v1beta1_job_template_spec import \
    V1beta1JobTemplateSpec
from kubernetes.client.models.v1beta1_json_schema_props import \
    V1beta1JSONSchemaProps
from kubernetes.client.models.v1beta1_lease import V1beta1Lease
from kubernetes.client.models.v1beta1_lease_list import V1beta1LeaseList
from kubernetes.client.models.v1beta1_lease_spec import V1beta1LeaseSpec
from kubernetes.client.models.v1beta1_local_subject_access_review import \
    V1beta1LocalSubjectAccessReview
from kubernetes.client.models.v1beta1_mutating_webhook import \
    V1beta1MutatingWebhook
from kubernetes.client.models.v1beta1_mutating_webhook_configuration import \
    V1beta1MutatingWebhookConfiguration
from kubernetes.client.models.v1beta1_mutating_webhook_configuration_list import \
    V1beta1MutatingWebhookConfigurationList
from kubernetes.client.models.v1beta1_network_policy import \
    V1beta1NetworkPolicy
from kubernetes.client.models.v1beta1_network_policy_egress_rule import \
    V1beta1NetworkPolicyEgressRule
from kubernetes.client.models.v1beta1_network_policy_ingress_rule import \
    V1beta1NetworkPolicyIngressRule
from kubernetes.client.models.v1beta1_network_policy_list import \
    V1beta1NetworkPolicyList
from kubernetes.client.models.v1beta1_network_policy_peer import \
    V1beta1NetworkPolicyPeer
from kubernetes.client.models.v1beta1_network_policy_port import \
    V1beta1NetworkPolicyPort
from kubernetes.client.models.v1beta1_network_policy_spec import \
    V1beta1NetworkPolicySpec
from kubernetes.client.models.v1beta1_non_resource_attributes import \
    V1beta1NonResourceAttributes
from kubernetes.client.models.v1beta1_non_resource_rule import \
    V1beta1NonResourceRule
from kubernetes.client.models.v1beta1_overhead import V1beta1Overhead
from kubernetes.client.models.v1beta1_pod_disruption_budget import \
    V1beta1PodDisruptionBudget
from kubernetes.client.models.v1beta1_pod_disruption_budget_list import \
    V1beta1PodDisruptionBudgetList
from kubernetes.client.models.v1beta1_pod_disruption_budget_spec import \
    V1beta1PodDisruptionBudgetSpec
from kubernetes.client.models.v1beta1_pod_disruption_budget_status import \
    V1beta1PodDisruptionBudgetStatus
from kubernetes.client.models.v1beta1_policy_rule import V1beta1PolicyRule
from kubernetes.client.models.v1beta1_priority_class import \
    V1beta1PriorityClass
from kubernetes.client.models.v1beta1_priority_class_list import \
    V1beta1PriorityClassList
from kubernetes.client.models.v1beta1_replica_set import V1beta1ReplicaSet
from kubernetes.client.models.v1beta1_replica_set_condition import \
    V1beta1ReplicaSetCondition
from kubernetes.client.models.v1beta1_replica_set_list import \
    V1beta1ReplicaSetList
from kubernetes.client.models.v1beta1_replica_set_spec import \
    V1beta1ReplicaSetSpec
from kubernetes.client.models.v1beta1_replica_set_status import \
    V1beta1ReplicaSetStatus
from kubernetes.client.models.v1beta1_resource_attributes import \
    V1beta1ResourceAttributes
from kubernetes.client.models.v1beta1_resource_rule import V1beta1ResourceRule
from kubernetes.client.models.v1beta1_role import V1beta1Role
from kubernetes.client.models.v1beta1_role_binding import V1beta1RoleBinding
from kubernetes.client.models.v1beta1_role_binding_list import \
    V1beta1RoleBindingList
from kubernetes.client.models.v1beta1_role_list import V1beta1RoleList
from kubernetes.client.models.v1beta1_role_ref import V1beta1RoleRef
from kubernetes.client.models.v1beta1_rolling_update_daemon_set import \
    V1beta1RollingUpdateDaemonSet
from kubernetes.client.models.v1beta1_rolling_update_stateful_set_strategy import \
    V1beta1RollingUpdateStatefulSetStrategy
from kubernetes.client.models.v1beta1_rule_with_operations import \
    V1beta1RuleWithOperations
from kubernetes.client.models.v1beta1_runtime_class import V1beta1RuntimeClass
from kubernetes.client.models.v1beta1_runtime_class_list import \
    V1beta1RuntimeClassList
from kubernetes.client.models.v1beta1_scheduling import V1beta1Scheduling
from kubernetes.client.models.v1beta1_self_subject_access_review import \
    V1beta1SelfSubjectAccessReview
from kubernetes.client.models.v1beta1_self_subject_access_review_spec import \
    V1beta1SelfSubjectAccessReviewSpec
from kubernetes.client.models.v1beta1_self_subject_rules_review import \
    V1beta1SelfSubjectRulesReview
from kubernetes.client.models.v1beta1_self_subject_rules_review_spec import \
    V1beta1SelfSubjectRulesReviewSpec
from kubernetes.client.models.v1beta1_stateful_set import V1beta1StatefulSet
from kubernetes.client.models.v1beta1_stateful_set_condition import \
    V1beta1StatefulSetCondition
from kubernetes.client.models.v1beta1_stateful_set_list import \
    V1beta1StatefulSetList
from kubernetes.client.models.v1beta1_stateful_set_spec import \
    V1beta1StatefulSetSpec
from kubernetes.client.models.v1beta1_stateful_set_status import \
    V1beta1StatefulSetStatus
from kubernetes.client.models.v1beta1_stateful_set_update_strategy import \
    V1beta1StatefulSetUpdateStrategy
from kubernetes.client.models.v1beta1_storage_class import V1beta1StorageClass
from kubernetes.client.models.v1beta1_storage_class_list import \
    V1beta1StorageClassList
from kubernetes.client.models.v1beta1_subject import V1beta1Subject
from kubernetes.client.models.v1beta1_subject_access_review import \
    V1beta1SubjectAccessReview
from kubernetes.client.models.v1beta1_subject_access_review_spec import \
    V1beta1SubjectAccessReviewSpec
from kubernetes.client.models.v1beta1_subject_access_review_status import \
    V1beta1SubjectAccessReviewStatus
from kubernetes.client.models.v1beta1_subject_rules_review_status import \
    V1beta1SubjectRulesReviewStatus
from kubernetes.client.models.v1beta1_token_review import V1beta1TokenReview
from kubernetes.client.models.v1beta1_token_review_spec import \
    V1beta1TokenReviewSpec
from kubernetes.client.models.v1beta1_token_review_status import \
    V1beta1TokenReviewStatus
from kubernetes.client.models.v1beta1_user_info import V1beta1UserInfo
from kubernetes.client.models.v1beta1_validating_webhook import \
    V1beta1ValidatingWebhook
from kubernetes.client.models.v1beta1_validating_webhook_configuration import \
    V1beta1ValidatingWebhookConfiguration
from kubernetes.client.models.v1beta1_validating_webhook_configuration_list import \
    V1beta1ValidatingWebhookConfigurationList
from kubernetes.client.models.v1beta1_volume_attachment import \
    V1beta1VolumeAttachment
from kubernetes.client.models.v1beta1_volume_attachment_list import \
    V1beta1VolumeAttachmentList
from kubernetes.client.models.v1beta1_volume_attachment_source import \
    V1beta1VolumeAttachmentSource
from kubernetes.client.models.v1beta1_volume_attachment_spec import \
    V1beta1VolumeAttachmentSpec
from kubernetes.client.models.v1beta1_volume_attachment_status import \
    V1beta1VolumeAttachmentStatus
from kubernetes.client.models.v1beta1_volume_error import V1beta1VolumeError
from kubernetes.client.models.v1beta1_volume_node_resources import \
    V1beta1VolumeNodeResources
from kubernetes.client.models.v1beta2_controller_revision import \
    V1beta2ControllerRevision
from kubernetes.client.models.v1beta2_controller_revision_list import \
    V1beta2ControllerRevisionList
from kubernetes.client.models.v1beta2_daemon_set import V1beta2DaemonSet
from kubernetes.client.models.v1beta2_daemon_set_condition import \
    V1beta2DaemonSetCondition
from kubernetes.client.models.v1beta2_daemon_set_list import \
    V1beta2DaemonSetList
from kubernetes.client.models.v1beta2_daemon_set_spec import \
    V1beta2DaemonSetSpec
from kubernetes.client.models.v1beta2_daemon_set_status import \
    V1beta2DaemonSetStatus
from kubernetes.client.models.v1beta2_daemon_set_update_strategy import \
    V1beta2DaemonSetUpdateStrategy
from kubernetes.client.models.v1beta2_deployment import V1beta2Deployment
from kubernetes.client.models.v1beta2_deployment_condition import \
    V1beta2DeploymentCondition
from kubernetes.client.models.v1beta2_deployment_list import \
    V1beta2DeploymentList
from kubernetes.client.models.v1beta2_deployment_spec import \
    V1beta2DeploymentSpec
from kubernetes.client.models.v1beta2_deployment_status import \
    V1beta2DeploymentStatus
from kubernetes.client.models.v1beta2_deployment_strategy import \
    V1beta2DeploymentStrategy
from kubernetes.client.models.v1beta2_replica_set import V1beta2ReplicaSet
from kubernetes.client.models.v1beta2_replica_set_condition import \
    V1beta2ReplicaSetCondition
from kubernetes.client.models.v1beta2_replica_set_list import \
    V1beta2ReplicaSetList
from kubernetes.client.models.v1beta2_replica_set_spec import \
    V1beta2ReplicaSetSpec
from kubernetes.client.models.v1beta2_replica_set_status import \
    V1beta2ReplicaSetStatus
from kubernetes.client.models.v1beta2_rolling_update_daemon_set import \
    V1beta2RollingUpdateDaemonSet
from kubernetes.client.models.v1beta2_rolling_update_deployment import \
    V1beta2RollingUpdateDeployment
from kubernetes.client.models.v1beta2_rolling_update_stateful_set_strategy import \
    V1beta2RollingUpdateStatefulSetStrategy
from kubernetes.client.models.v1beta2_scale import V1beta2Scale
from kubernetes.client.models.v1beta2_scale_spec import V1beta2ScaleSpec
from kubernetes.client.models.v1beta2_scale_status import V1beta2ScaleStatus
from kubernetes.client.models.v1beta2_stateful_set import V1beta2StatefulSet
from kubernetes.client.models.v1beta2_stateful_set_condition import \
    V1beta2StatefulSetCondition
from kubernetes.client.models.v1beta2_stateful_set_list import \
    V1beta2StatefulSetList
from kubernetes.client.models.v1beta2_stateful_set_spec import \
    V1beta2StatefulSetSpec
from kubernetes.client.models.v1beta2_stateful_set_status import \
    V1beta2StatefulSetStatus
from kubernetes.client.models.v1beta2_stateful_set_update_strategy import \
    V1beta2StatefulSetUpdateStrategy
from kubernetes.client.models.v2alpha1_cron_job import V2alpha1CronJob
from kubernetes.client.models.v2alpha1_cron_job_list import V2alpha1CronJobList
from kubernetes.client.models.v2alpha1_cron_job_spec import V2alpha1CronJobSpec
from kubernetes.client.models.v2alpha1_cron_job_status import \
    V2alpha1CronJobStatus
from kubernetes.client.models.v2alpha1_job_template_spec import \
    V2alpha1JobTemplateSpec
from kubernetes.client.models.v2beta1_cross_version_object_reference import \
    V2beta1CrossVersionObjectReference
from kubernetes.client.models.v2beta1_external_metric_source import \
    V2beta1ExternalMetricSource
from kubernetes.client.models.v2beta1_external_metric_status import \
    V2beta1ExternalMetricStatus
from kubernetes.client.models.v2beta1_horizontal_pod_autoscaler import \
    V2beta1HorizontalPodAutoscaler
from kubernetes.client.models.v2beta1_horizontal_pod_autoscaler_condition import \
    V2beta1HorizontalPodAutoscalerCondition
from kubernetes.client.models.v2beta1_horizontal_pod_autoscaler_list import \
    V2beta1HorizontalPodAutoscalerList
from kubernetes.client.models.v2beta1_horizontal_pod_autoscaler_spec import \
    V2beta1HorizontalPodAutoscalerSpec
from kubernetes.client.models.v2beta1_horizontal_pod_autoscaler_status import \
    V2beta1HorizontalPodAutoscalerStatus
from kubernetes.client.models.v2beta1_metric_spec import V2beta1MetricSpec
from kubernetes.client.models.v2beta1_metric_status import V2beta1MetricStatus
from kubernetes.client.models.v2beta1_object_metric_source import \
    V2beta1ObjectMetricSource
from kubernetes.client.models.v2beta1_object_metric_status import \
    V2beta1ObjectMetricStatus
from kubernetes.client.models.v2beta1_pods_metric_source import \
    V2beta1PodsMetricSource
from kubernetes.client.models.v2beta1_pods_metric_status import \
    V2beta1PodsMetricStatus
from kubernetes.client.models.v2beta1_resource_metric_source import \
    V2beta1ResourceMetricSource
from kubernetes.client.models.v2beta1_resource_metric_status import \
    V2beta1ResourceMetricStatus
from kubernetes.client.models.v2beta2_cross_version_object_reference import \
    V2beta2CrossVersionObjectReference
from kubernetes.client.models.v2beta2_external_metric_source import \
    V2beta2ExternalMetricSource
from kubernetes.client.models.v2beta2_external_metric_status import \
    V2beta2ExternalMetricStatus
from kubernetes.client.models.v2beta2_horizontal_pod_autoscaler import \
    V2beta2HorizontalPodAutoscaler
from kubernetes.client.models.v2beta2_horizontal_pod_autoscaler_condition import \
    V2beta2HorizontalPodAutoscalerCondition
from kubernetes.client.models.v2beta2_horizontal_pod_autoscaler_list import \
    V2beta2HorizontalPodAutoscalerList
from kubernetes.client.models.v2beta2_horizontal_pod_autoscaler_spec import \
    V2beta2HorizontalPodAutoscalerSpec
from kubernetes.client.models.v2beta2_horizontal_pod_autoscaler_status import \
    V2beta2HorizontalPodAutoscalerStatus
from kubernetes.client.models.v2beta2_metric_identifier import \
    V2beta2MetricIdentifier
from kubernetes.client.models.v2beta2_metric_spec import V2beta2MetricSpec
from kubernetes.client.models.v2beta2_metric_status import V2beta2MetricStatus
from kubernetes.client.models.v2beta2_metric_target import V2beta2MetricTarget
from kubernetes.client.models.v2beta2_metric_value_status import \
    V2beta2MetricValueStatus
from kubernetes.client.models.v2beta2_object_metric_source import \
    V2beta2ObjectMetricSource
from kubernetes.client.models.v2beta2_object_metric_status import \
    V2beta2ObjectMetricStatus
from kubernetes.client.models.v2beta2_pods_metric_source import \
    V2beta2PodsMetricSource
from kubernetes.client.models.v2beta2_pods_metric_status import \
    V2beta2PodsMetricStatus
from kubernetes.client.models.v2beta2_resource_metric_source import \
    V2beta2ResourceMetricSource
from kubernetes.client.models.v2beta2_resource_metric_status import \
    V2beta2ResourceMetricStatus
from kubernetes.client.models.version_info import VersionInfo