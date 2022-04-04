import openstack
import os

class create_network:
    conn = openstack.connect(cloud='admin')
    
    def create_networks(self,network_name,subnet_name,IP,gateway):
        try:
            print("Create Network : {}".format(network_name))

            example_network = self.conn.network.create_network(
                name=network_name)

            print(example_network)

            print("Create Subnet :{}".format(subnet_name))

            example_subnet = self.conn.network.create_subnet(
                name=subnet_name,
                network_id=example_network.id,
                ip_version='4',
                cidr=IP,
                gateway_ip=gateway)

            print(example_subnet)

            print("Creating a Router ")

            create_router(subnet_name)
        except Exception as e:
            print("Network {} creation failed with error {} ".format(network_name,str(e)))
            
def create_router(subnet_name):
    try:
        routers = os.popen('openstack router list').read()
        router_name = 'lab8-connect'
        
        if router_name not in routers:
            os.popen('openstack router create ' + router_name).read()
            os.popen('openstack router set SDN_LAB8 --external-gateway public').read()
        os.popen('openstack router add subnet ' + router_name + ' ' + subnet_name).read()    
    except Exception as e:
        print("Failed to add router with subnet {} with error {}".format(subnet_name,str(e)))
    
