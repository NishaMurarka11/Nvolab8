import os
import openstack
from Create_network import create_network
from Create_vm import create_vm
from Create_Sec_Grp import create_secGrp
from Create_Frr import create_frr
from Create_Ryu import ryu_bgp

class lab8:
    
    
    def create_instance(self,name,network):
        vm = create_vm()
        ret = vm.create_server(name,network)
        
        
    def create_networks(self,network_name,subnet_name,IP,gateway):
        network = create_network()
        ret = network.create_networks(network_name,subnet_name,IP,gateway)
    
    def create_security_grp(self,vm_name):
        sec_grp = create_secGrp()
        sec_grp = sec_grp.create_secGrp(vm_name)
    
    def call_openstack(self):
        network_details = [{'network_name':'lab8_net1','subnet_name':'lab8_subnet1','IP':'20.20.1.0/24','gateway':'20.20.1.1'},
                           {'network_name':'lab8_net2','subnet_name':'lab8_subnet2','IP':'20.20.2.0/24','gateway':'20.20.2.1'}]
                           #{'network_name':'lab8_net3','subnet_name':'lab8_subnet3','IP':'20.20.3.0/24','gateway':'20.20.3.1'}]
        instance_network = [{'instance_name':'lab8_instance1','network_name':'lab8_net1'},
                            {'instance_name':'lab8_instance2','network_name':'lab8_net1'},
                            {'instance_name':'lab8_instance3','network_name':'lab8_net2'}]
        for network in network_details:
            self.create_networks(network['network_name'],network['subnet_name'],network['IP'],network['gateway'])
        for instance in instance_network:
            self.create_instance(instance['instance_name'],instance['network_name'])
            self.create_security_grp(instance['instance_name'])
            
    def bgp_docker(self):
        # Start Frr docker 
        frr_docker = create_frr()
        frr_docker.create_bgp()
        # Start Ryu 
        ryu_docker = ryu_bgp()
        ryu_docker.create_bgp_speaker()
        
        
        
    
       
instance = lab8()
instance.call_openstack()
instance.bgp_docker()
