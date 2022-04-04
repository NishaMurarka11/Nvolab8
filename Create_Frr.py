import os
import time

class create_frr:
    
    def create_bgp(self):
        try:
            docker_name = 'frr_bgp'
            cwd = os.getcwd()
            frr_path=cwd+'/frr.conf'
            daemons_path=cwd+'/daemons'
            try:
                os.popen('sudo docker stop '+ docker_name).read()
                os.popen('sudo docker rm ' + docker_name).read()
            except:
                pass
            os.popen('sudo docker run -v '+ frr_path +':/etc/frr/frr.conf -v '+ daemons_path +':/etc/frr/daemons -itd --privileged --name '+ docker_name +' frrouting/frr-debian').read()
            time.sleep(5)
            #os.system('sudo docker exec -it '+ docker_name +' vtysh -c "show ip bgp neighbor"')
            os.system('sudo docker exec -it '+ docker_name +' vtysh -c "show ip bgp"')
        except Exception as e:
            print("error bringing up docker FRR with error {}".format(str(e)))
