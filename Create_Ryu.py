import os
class ryu_bgp:
    def create_bgp_speaker():
        docker_name = 'ryu'
        conf_file = '/home/nvolab/lab/ryu_bgp.py'
        try:
            os.popen('sudo docker stop ' + docker_name).read()
            os.popen('sudo docker rm ' + docker_name).read()
            os.popen('sudo docker run -tid -v '+ conf_file +':/root/ryu/ryu/services/protocols/bgp/ryu_bgp.py --name '+ docker_name +' ryu-work').read()
            os.system('sudo docker exec -it ryu_sdn_bgp ryu-manager ./ryu/ryu/services/protocols/bgp/application.py --bgp-app-config-file ryu/ryu/services/protocols/bgp/ryu_bgp.py')
        except Exception as e:
            print("Error creating sdn controllerx with error {}".format(str(e)))