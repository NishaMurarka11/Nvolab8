import os

class create_frr:
    
    def create_bgp():
        try:
            docker_name = 'frr_bgp'
            frr_path = "/home/nvolab/lab/frr_conf"
            daemons_path = "/home/nvolab/lab/daemons"
            os.popen('sudo docker stop '+ docker_name).read()
            os.popen('sudo docker rm ' + docker_name).read()
            os.popen('sudo docker run -v ' + frr_path +':/etc/frr/frr.conf -itd --privileged --name '+ docker_name +' frrouting/frr-debian').read()
            os.popen('sudo docker cp '+ daemons_path + ' '+ docker_name + ':/etc/frr').read()
            os.popen('sudo docker restart '+ docker_name)
            os.system('sudo docker exec -it '+ docker_name +' vtysh -c "show ip bgp neighbor"')
            os.system('sudo docker exec -it '+ docker_name +' vtysh -c "show ip bgp"')
        except Exception as e:
            print("error bringing up docker FRR with error {}".format(str(e)))