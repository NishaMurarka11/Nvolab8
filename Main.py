import os
import openstack
from Create_network import create_network
from Create_vm import create_vm
from Create_Sec_Grp import create_secGrp


class lab8:
    
    
    def create_instance(self,name,network):
        vm = create_vm()
        ret = vm.create_server(name,network)
        #print(ret)
        
    def create_networks(self,network_name,subnet_name,IP,gateway):
        network = create_network()
        ret = network.create_networks(network_name,subnet_name,IP,gateway)
    
    def create_security_grp(self,vm_name):
        sec_grp = create_secGrp()
        sec_grp = sec_grp.create_secGrp(vm_name)
    
    def call_openstack(self):
        #network_details = {'network_name':'lab8_net1','subnet_name':'lab8_subnet1','IP':'20.20.20.0/24','gateway':'20.20.20.1'}
        #self.create_networks(network_details['network_name'],network_details['subnet_name'],network_details['IP'],network_details['gateway'])
        #self.create_instance("lab8_instance1","lab8_net1")
        self.create_security_grp("lab8_instance1")
        

instance = lab8()
instance.call_openstack()
