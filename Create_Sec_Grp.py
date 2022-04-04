import openstack 
import os


class create_secGrp:

    conn = openstack.connect(cloud='admin')
    
    def create_secGrp(self,vm_name):
        try:
            sec_grp = os.popen('openstack security group list').read()
            sec_grp_name='lab-security'
            if sec_grp_name not in sec_grp:
                new_sec_group = self.conn.network.create_security_group(
                name='lab-security')
            
                print(new_sec_group)
                example_rule = self.conn.network.create_security_group_rule(
                    security_group_id=new_sec_group.id,
                    direction='ingress',
                    remote_ip_prefix='0.0.0.0/0',
                    protocol='icmp',
                    port_range_max=None,
                    port_range_min=None,
                    ethertype='IPv4')
                print(example_rule)
            os.popen('openstack server add security group ' + vm_name + ' ' + sec_grp_name ).read()
        except Exception as e:
            print("Failed to create security group with error {}".format(str(e)))
