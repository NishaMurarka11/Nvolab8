import openstack
import os
import errno
import subprocess
from time import sleep


class create_vm:
    
    conn = openstack.connect(cloud='admin')
        
    def create_keypair(self):
        keypair = self.conn.compute.find_keypair("lab8")

        if not keypair:
            print("Create Key Pair:")
            keypair = self.conn.compute.create_keypair(name="lab8")
            print(keypair)
            try:
                os.mkdir("/home/nvolab/.ssh")
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise e

            with open("lab8.pem", 'w') as f:
                f.write("%s" % keypair.private_key)
            os.chmod("lab8.pem", 0o400)
        return keypair
    
    def create_server(self,name,network):
        try:
            image = self.conn.compute.find_image("cirros-0.5.2-x86_64-disk")
            flavor = self.conn.compute.find_flavor("m1.tiny")
            network = self.conn.network.find_network(network)
            keypair = self.create_keypair()
            
            server = self.conn.compute.create_server(
                name=name, image_id=image.id, flavor_id=flavor.id,
                networks=[{"uuid": network.id}], key_name=keypair.name)
            server = self.conn.compute.wait_for_server(server)
            print("Server {} created on {} with IP {}".format(name,network,server.access_ipv4 ))
        except Exception as e:
            print("failed to create sever {} with error {}".format(name,str(e)))
        return "OK"
