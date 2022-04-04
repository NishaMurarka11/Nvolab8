# Openstack Objective
Below is the Screen capture of the Program Main.Py that does following 
1) Create two new networks and subnetwork and connect it external gateway (public network ) using router
2) Create three instance two of them are in same subnet and one in a different subnet
3) Create a security group that allow all ICPM and add the group to all instaces. 

```
nvolab@nvolab:~/Nvolab8$ python3 Main.py 
Create Network : lab8_net1
+---------------------------+--------------------------------------+
| Field                     | Value                                |
+---------------------------+--------------------------------------+
| admin_state_up            | UP                                   |
| availability_zone_hints   |                                      |
| availability_zones        |                                      |
| created_at                | 2022-04-04T19:21:16Z                 |
| description               |                                      |
| dns_domain                | None                                 |
| id                        | d88cf6bf-bb85-46dd-a79e-32990683a5aa |
| ipv4_address_scope        | None                                 |
| ipv6_address_scope        | None                                 |
| is_default                | None                                 |
| is_vlan_transparent       | None                                 |
| mtu                       | 1450                                 |
| name                      | lab8_net1                            |
| port_security_enabled     | True                                 |
| project_id                | bdb45f9678b747a1a70ca17d272b0e81     |
| provider:network_type     | vxlan                                |
| provider:physical_network | None                                 |
| provider:segmentation_id  | 584                                  |
| qos_policy_id             | None                                 |
| revision_number           | 1                                    |
| router:external           | Internal                             |
| segments                  | None                                 |
| shared                    | False                                |
| status                    | ACTIVE                               |
| subnets                   |                                      |
| tags                      |                                      |
| updated_at                | 2022-04-04T19:21:16Z                 |
+---------------------------+--------------------------------------+
Create Subnet :lab8_subnet1
+----------------------+--------------------------------------+
| Field                | Value                                |
+----------------------+--------------------------------------+
| allocation_pools     | 20.20.1.2-20.20.1.254                |
| cidr                 | 20.20.1.0/24                         |
| created_at           | 2022-04-04T19:21:21Z                 |
| description          |                                      |
| dns_nameservers      |                                      |
| dns_publish_fixed_ip | None                                 |
| enable_dhcp          | True                                 |
| gateway_ip           | 20.20.1.1                            |
| host_routes          |                                      |
| id                   | a6c081bf-e945-4be3-adcb-b8511f65c69d |
| ip_version           | 4                                    |
| ipv6_address_mode    | None                                 |
| ipv6_ra_mode         | None                                 |
| name                 | lab8_subnet1                         |
| network_id           | d88cf6bf-bb85-46dd-a79e-32990683a5aa |
| prefix_length        | None                                 |
| project_id           | bdb45f9678b747a1a70ca17d272b0e81     |
| revision_number      | 0                                    |
| segment_id           | None                                 |
| service_types        |                                      |
| subnetpool_id        | None                                 |
| tags                 |                                      |
| updated_at           | 2022-04-04T19:21:21Z                 |
+----------------------+--------------------------------------+
Creating a Router lab8-connect
No Router found for SDN_LAB8
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Field                   | Value                                                                                                                                 |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| admin_state_up          | UP                                                                                                                                    |
| availability_zone_hints |                                                                                                                                       |
| availability_zones      | nova                                                                                                                                  |
| created_at              | 2022-04-04T19:21:28Z                                                                                                                  |
| description             |                                                                                                                                       |
| distributed             | False                                                                                                                                 |
| external_gateway_info   | null                                                                                                                                  |
| flavor_id               | None                                                                                                                                  |
| ha                      | False                                                                                                                                 |
| id                      | a7492748-9dc0-4c99-b4da-fb4d5c4c0bc2                                                                                                  |
| interfaces_info         | [{"port_id": "7d4d0bdb-242b-41f5-8fcd-3bae240109cc", "ip_address": "20.20.1.1", "subnet_id": "a6c081bf-e945-4be3-adcb-b8511f65c69d"}] |
| name                    | lab8-connect                                                                                                                          |
| project_id              | bdb45f9678b747a1a70ca17d272b0e81                                                                                                      |
| revision_number         | 2                                                                                                                                     |
| routes                  |                                                                                                                                       |
| status                  | ACTIVE                                                                                                                                |
| tags                    |                                                                                                                                       |
| updated_at              | 2022-04-04T19:21:34Z                                                                                                                  |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
Create Network : lab8_net2
+---------------------------+--------------------------------------+
| Field                     | Value                                |
+---------------------------+--------------------------------------+
| admin_state_up            | UP                                   |
| availability_zone_hints   |                                      |
| availability_zones        |                                      |
| created_at                | 2022-04-04T19:21:40Z                 |
| description               |                                      |
| dns_domain                | None                                 |
| id                        | 3b9f88f9-6f8e-4a01-850b-055503e0e872 |
| ipv4_address_scope        | None                                 |
| ipv6_address_scope        | None                                 |
| is_default                | None                                 |
| is_vlan_transparent       | None                                 |
| mtu                       | 1450                                 |
| name                      | lab8_net2                            |
| port_security_enabled     | True                                 |
| project_id                | bdb45f9678b747a1a70ca17d272b0e81     |
| provider:network_type     | vxlan                                |
| provider:physical_network | None                                 |
| provider:segmentation_id  | 11                                   |
| qos_policy_id             | None                                 |
| revision_number           | 1                                    |
| router:external           | Internal                             |
| segments                  | None                                 |
| shared                    | False                                |
| status                    | ACTIVE                               |
| subnets                   |                                      |
| tags                      |                                      |
| updated_at                | 2022-04-04T19:21:40Z                 |
+---------------------------+--------------------------------------+
Create Subnet :lab8_subnet2
+----------------------+--------------------------------------+
| Field                | Value                                |
+----------------------+--------------------------------------+
| allocation_pools     | 20.20.2.2-20.20.2.254                |
| cidr                 | 20.20.2.0/24                         |
| created_at           | 2022-04-04T19:21:45Z                 |
| description          |                                      |
| dns_nameservers      |                                      |
| dns_publish_fixed_ip | None                                 |
| enable_dhcp          | True                                 |
| gateway_ip           | 20.20.2.1                            |
| host_routes          |                                      |
| id                   | daef4237-5ac1-42c8-871f-70edf6d49aec |
| ip_version           | 4                                    |
| ipv6_address_mode    | None                                 |
| ipv6_ra_mode         | None                                 |
| name                 | lab8_subnet2                         |
| network_id           | 3b9f88f9-6f8e-4a01-850b-055503e0e872 |
| prefix_length        | None                                 |
| project_id           | bdb45f9678b747a1a70ca17d272b0e81     |
| revision_number      | 0                                    |
| segment_id           | None                                 |
| service_types        |                                      |
| subnetpool_id        | None                                 |
| tags                 |                                      |
| updated_at           | 2022-04-04T19:21:45Z                 |
+----------------------+--------------------------------------+
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                   | Value                                                                                                                                                                                                                                                                      |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| admin_state_up          | UP                                                                                                                                                                                                                                                                         |
| availability_zone_hints |                                                                                                                                                                                                                                                                            |
| availability_zones      | nova                                                                                                                                                                                                                                                                       |
| created_at              | 2022-04-04T19:21:28Z                                                                                                                                                                                                                                                       |
| description             |                                                                                                                                                                                                                                                                            |
| distributed             | False                                                                                                                                                                                                                                                                      |
| external_gateway_info   | null                                                                                                                                                                                                                                                                       |
| flavor_id               | None                                                                                                                                                                                                                                                                       |
| ha                      | False                                                                                                                                                                                                                                                                      |
| id                      | a7492748-9dc0-4c99-b4da-fb4d5c4c0bc2                                                                                                                                                                                                                                       |
| interfaces_info         | [{"port_id": "2db05f84-ff7b-43db-9ac4-4f7ed52ac92d", "ip_address": "20.20.2.1", "subnet_id": "daef4237-5ac1-42c8-871f-70edf6d49aec"}, {"port_id": "7d4d0bdb-242b-41f5-8fcd-3bae240109cc", "ip_address": "20.20.1.1", "subnet_id": "a6c081bf-e945-4be3-adcb-b8511f65c69d"}] |
| name                    | lab8-connect                                                                                                                                                                                                                                                               |
| project_id              | bdb45f9678b747a1a70ca17d272b0e81                                                                                                                                                                                                                                           |
| revision_number         | 3                                                                                                                                                                                                                                                                          |
| routes                  |                                                                                                                                                                                                                                                                            |
| status                  | ACTIVE                                                                                                                                                                                                                                                                     |
| tags                    |                                                                                                                                                                                                                                                                            |
| updated_at              | 2022-04-04T19:21:54Z                                                                                                                                                                                                                                                       |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
Server lab8_instance1 created on openstack.network.v2.network.Network(id=d88cf6bf-bb85-46dd-a79e-32990683a5aa, name=lab8_net1, admin_state_up=True, mtu=1450, status=ACTIVE, subnets=['a6c081bf-e945-4be3-adcb-b8511f65c69d'], shared=False, availability_zone_hints=[], availability_zones=['nova'], ipv4_address_scope=None, ipv6_address_scope=None, router:external=False, description=, port_security_enabled=True, tags=[], created_at=2022-04-04T19:21:16Z, updated_at=2022-04-04T19:21:21Z, revision_number=2, project_id=bdb45f9678b747a1a70ca17d272b0e81, provider:network_type=vxlan, provider:physical_network=None, provider:segmentation_id=584, location=Munch({'cloud': 'admin', 'region_name': 'RegionOne', 'zone': None, 'project': Munch({'id': 'bdb45f9678b747a1a70ca17d272b0e81', 'name': 'admin', 'domain_id': None, 'domain_name': 'default'})})) with IP 
+-------------------------------------+-----------------------------------------------------------------+
| Field                               | Value                                                           |
+-------------------------------------+-----------------------------------------------------------------+
| OS-DCF:diskConfig                   | MANUAL                                                          |
| OS-EXT-AZ:availability_zone         | nova                                                            |
| OS-EXT-SRV-ATTR:host                | nvolab                                                          |
| OS-EXT-SRV-ATTR:hypervisor_hostname | nvolab                                                          |
| OS-EXT-SRV-ATTR:instance_name       | instance-0000000c                                               |
| OS-EXT-STS:power_state              | Running                                                         |
| OS-EXT-STS:task_state               | None                                                            |
| OS-EXT-STS:vm_state                 | active                                                          |
| OS-SRV-USG:launched_at              | 2022-04-04T19:22:09.000000                                      |
| OS-SRV-USG:terminated_at            | None                                                            |
| accessIPv4                          |                                                                 |
| accessIPv6                          |                                                                 |
| addresses                           | lab8_net1=20.20.1.38                                            |
| config_drive                        |                                                                 |
| created                             | 2022-04-04T19:22:01Z                                            |
| flavor                              | m1.tiny (1)                                                     |
| hostId                              | 3b2f13ab96ece636794521b9e8fcab1c616546a9b16fdb60590fe18c        |
| id                                  | 92d68f4c-bb9a-4b6b-9ab1-8126a05ff279                            |
| image                               | cirros-0.5.2-x86_64-disk (aec9eb56-71b0-402d-8b91-eacb2e1f057c) |
| key_name                            | lab8                                                            |
| name                                | lab8_instance1                                                  |
| progress                            | 0                                                               |
| project_id                          | bdb45f9678b747a1a70ca17d272b0e81                                |
| properties                          |                                                                 |
| security_groups                     | name='default'                                                  |
| status                              | ACTIVE                                                          |
| updated                             | 2022-04-04T19:22:10Z                                            |
| user_id                             | 9f72570802564cc7a66a14c3138fc04f                                |
| volumes_attached                    |                                                                 |
+-------------------------------------+-----------------------------------------------------------------+
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field           | Value                                                                                                                                                                                                 |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| created_at      | 2022-04-04T19:13:52Z                                                                                                                                                                                  |
| description     |                                                                                                                                                                                                       |
| id              | 10aeea83-8b25-45dc-b743-d20d3504ae8c                                                                                                                                                                  |
| name            | lab-security                                                                                                                                                                                          |
| project_id      | bdb45f9678b747a1a70ca17d272b0e81                                                                                                                                                                      |
| revision_number | 2                                                                                                                                                                                                     |
| rules           | created_at='2022-04-04T19:13:52Z', direction='egress', ethertype='IPv4', id='3cfcbae6-88eb-4347-9ec4-20f78f3a5d34', updated_at='2022-04-04T19:13:52Z'                                                 |
|                 | created_at='2022-04-04T19:13:52Z', direction='egress', ethertype='IPv6', id='74f393d8-eb1c-49db-a3fb-feb80d5210ad', updated_at='2022-04-04T19:13:52Z'                                                 |
|                 | created_at='2022-04-04T19:13:53Z', direction='ingress', ethertype='IPv4', id='7667476a-ffe0-4184-8e1e-79853c6194dc', protocol='icmp', remote_ip_prefix='0.0.0.0/0', updated_at='2022-04-04T19:13:53Z' |
| stateful        | True                                                                                                                                                                                                  |
| tags            | []                                                                                                                                                                                                    |
| updated_at      | 2022-04-04T19:13:53Z                                                                                                                                                                                  |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
Server lab8_instance2 created on openstack.network.v2.network.Network(id=d88cf6bf-bb85-46dd-a79e-32990683a5aa, name=lab8_net1, admin_state_up=True, mtu=1450, status=ACTIVE, subnets=['a6c081bf-e945-4be3-adcb-b8511f65c69d'], shared=False, availability_zone_hints=[], availability_zones=['nova'], ipv4_address_scope=None, ipv6_address_scope=None, router:external=False, description=, port_security_enabled=True, tags=[], created_at=2022-04-04T19:21:16Z, updated_at=2022-04-04T19:21:21Z, revision_number=2, project_id=bdb45f9678b747a1a70ca17d272b0e81, provider:network_type=vxlan, provider:physical_network=None, provider:segmentation_id=584, location=Munch({'cloud': 'admin', 'region_name': 'RegionOne', 'zone': None, 'project': Munch({'id': 'bdb45f9678b747a1a70ca17d272b0e81', 'name': 'admin', 'domain_id': None, 'domain_name': 'default'})})) with IP 
+-------------------------------------+-----------------------------------------------------------------+
| Field                               | Value                                                           |
+-------------------------------------+-----------------------------------------------------------------+
| OS-DCF:diskConfig                   | MANUAL                                                          |
| OS-EXT-AZ:availability_zone         | nova                                                            |
| OS-EXT-SRV-ATTR:host                | nvolab                                                          |
| OS-EXT-SRV-ATTR:hypervisor_hostname | nvolab                                                          |
| OS-EXT-SRV-ATTR:instance_name       | instance-0000000d                                               |
| OS-EXT-STS:power_state              | Running                                                         |
| OS-EXT-STS:task_state               | None                                                            |
| OS-EXT-STS:vm_state                 | active                                                          |
| OS-SRV-USG:launched_at              | 2022-04-04T19:22:33.000000                                      |
| OS-SRV-USG:terminated_at            | None                                                            |
| accessIPv4                          |                                                                 |
| accessIPv6                          |                                                                 |
| addresses                           | lab8_net1=20.20.1.39                                            |
| config_drive                        |                                                                 |
| created                             | 2022-04-04T19:22:25Z                                            |
| flavor                              | m1.tiny (1)                                                     |
| hostId                              | 3b2f13ab96ece636794521b9e8fcab1c616546a9b16fdb60590fe18c        |
| id                                  | 0951d36b-68c8-4086-93bf-94e6eabe8712                            |
| image                               | cirros-0.5.2-x86_64-disk (aec9eb56-71b0-402d-8b91-eacb2e1f057c) |
| key_name                            | lab8                                                            |
| name                                | lab8_instance2                                                  |
| progress                            | 0                                                               |
| project_id                          | bdb45f9678b747a1a70ca17d272b0e81                                |
| properties                          |                                                                 |
| security_groups                     | name='default'                                                  |
| status                              | ACTIVE                                                          |
| updated                             | 2022-04-04T19:22:34Z                                            |
| user_id                             | 9f72570802564cc7a66a14c3138fc04f                                |
| volumes_attached                    |                                                                 |
+-------------------------------------+-----------------------------------------------------------------+
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field           | Value                                                                                                                                                                                                 |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| created_at      | 2022-04-04T19:13:52Z                                                                                                                                                                                  |
| description     |                                                                                                                                                                                                       |
| id              | 10aeea83-8b25-45dc-b743-d20d3504ae8c                                                                                                                                                                  |
| name            | lab-security                                                                                                                                                                                          |
| project_id      | bdb45f9678b747a1a70ca17d272b0e81                                                                                                                                                                      |
| revision_number | 2                                                                                                                                                                                                     |
| rules           | created_at='2022-04-04T19:13:52Z', direction='egress', ethertype='IPv4', id='3cfcbae6-88eb-4347-9ec4-20f78f3a5d34', updated_at='2022-04-04T19:13:52Z'                                                 |
|                 | created_at='2022-04-04T19:13:52Z', direction='egress', ethertype='IPv6', id='74f393d8-eb1c-49db-a3fb-feb80d5210ad', updated_at='2022-04-04T19:13:52Z'                                                 |
|                 | created_at='2022-04-04T19:13:53Z', direction='ingress', ethertype='IPv4', id='7667476a-ffe0-4184-8e1e-79853c6194dc', protocol='icmp', remote_ip_prefix='0.0.0.0/0', updated_at='2022-04-04T19:13:53Z' |
| stateful        | True                                                                                                                                                                                                  |
| tags            | []                                                                                                                                                                                                    |
| updated_at      | 2022-04-04T19:13:53Z                                                                                                                                                                                  |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
Server lab8_instance3 created on openstack.network.v2.network.Network(id=3b9f88f9-6f8e-4a01-850b-055503e0e872, name=lab8_net2, admin_state_up=True, mtu=1450, status=ACTIVE, subnets=['daef4237-5ac1-42c8-871f-70edf6d49aec'], shared=False, availability_zone_hints=[], availability_zones=['nova'], ipv4_address_scope=None, ipv6_address_scope=None, router:external=False, description=, port_security_enabled=True, tags=[], created_at=2022-04-04T19:21:40Z, updated_at=2022-04-04T19:21:45Z, revision_number=2, project_id=bdb45f9678b747a1a70ca17d272b0e81, provider:network_type=vxlan, provider:physical_network=None, provider:segmentation_id=11, location=Munch({'cloud': 'admin', 'region_name': 'RegionOne', 'zone': None, 'project': Munch({'id': 'bdb45f9678b747a1a70ca17d272b0e81', 'name': 'admin', 'domain_id': None, 'domain_name': 'default'})})) with IP 
+-------------------------------------+-----------------------------------------------------------------+
| Field                               | Value                                                           |
+-------------------------------------+-----------------------------------------------------------------+
| OS-DCF:diskConfig                   | MANUAL                                                          |
| OS-EXT-AZ:availability_zone         | nova                                                            |
| OS-EXT-SRV-ATTR:host                | nvolab                                                          |
| OS-EXT-SRV-ATTR:hypervisor_hostname | nvolab                                                          |
| OS-EXT-SRV-ATTR:instance_name       | instance-0000000e                                               |
| OS-EXT-STS:power_state              | Running                                                         |
| OS-EXT-STS:task_state               | None                                                            |
| OS-EXT-STS:vm_state                 | active                                                          |
| OS-SRV-USG:launched_at              | 2022-04-04T19:22:56.000000                                      |
| OS-SRV-USG:terminated_at            | None                                                            |
| accessIPv4                          |                                                                 |
| accessIPv6                          |                                                                 |
| addresses                           | lab8_net2=20.20.2.173                                           |
| config_drive                        |                                                                 |
| created                             | 2022-04-04T19:22:48Z                                            |
| flavor                              | m1.tiny (1)                                                     |
| hostId                              | 3b2f13ab96ece636794521b9e8fcab1c616546a9b16fdb60590fe18c        |
| id                                  | 07186d00-c4ba-4c93-9356-96e191d98e20                            |
| image                               | cirros-0.5.2-x86_64-disk (aec9eb56-71b0-402d-8b91-eacb2e1f057c) |
| key_name                            | lab8                                                            |
| name                                | lab8_instance3                                                  |
| progress                            | 0                                                               |
| project_id                          | bdb45f9678b747a1a70ca17d272b0e81                                |
| properties                          |                                                                 |
| security_groups                     | name='default'                                                  |
| status                              | ACTIVE                                                          |
| updated                             | 2022-04-04T19:22:57Z                                            |
| user_id                             | 9f72570802564cc7a66a14c3138fc04f                                |
| volumes_attached                    |                                                                 |
+-------------------------------------+-----------------------------------------------------------------+
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field           | Value                                                                                                                                                                                                 |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| created_at      | 2022-04-04T19:13:52Z                                                                                                                                                                                  |
| description     |                                                                                                                                                                                                       |
| id              | 10aeea83-8b25-45dc-b743-d20d3504ae8c                                                                                                                                                                  |
| name            | lab-security                                                                                                                                                                                          |
| project_id      | bdb45f9678b747a1a70ca17d272b0e81                                                                                                                                                                      |
| revision_number | 2                                                                                                                                                                                                     |
| rules           | created_at='2022-04-04T19:13:52Z', direction='egress', ethertype='IPv4', id='3cfcbae6-88eb-4347-9ec4-20f78f3a5d34', updated_at='2022-04-04T19:13:52Z'                                                 |
|                 | created_at='2022-04-04T19:13:52Z', direction='egress', ethertype='IPv6', id='74f393d8-eb1c-49db-a3fb-feb80d5210ad', updated_at='2022-04-04T19:13:52Z'                                                 |
|                 | created_at='2022-04-04T19:13:53Z', direction='ingress', ethertype='IPv4', id='7667476a-ffe0-4184-8e1e-79853c6194dc', protocol='icmp', remote_ip_prefix='0.0.0.0/0', updated_at='2022-04-04T19:13:53Z' |
| stateful        | True                                                                                                                                                                                                  |
| tags            | []                                                                                                                                                                                                    |
| updated_at      | 2022-04-04T19:13:53Z                                                                                                                                                                                  |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
nvolab@nvolab:~/Nvolab8$ 

```

## Checking Connectivity between two VM in same network and differnt network 
![alt text](https://github.com/NishaMurarka11/Nvolab8/blob/master/VM_Connectivity.png)
![alt text](https://github.com/NishaMurarka11/Nvolab8/blob/master/VM2_connectivity.png)

# BGP between Ryu Sdn Controller and FRR running as container
![alt_text](https://github.com/NishaMurarka11/Nvolab8/blob/master/BGP_LOG.png)
![alt_text](https://github.com/NishaMurarka11/Nvolab8/blob/master/BGP_FRR.png)

