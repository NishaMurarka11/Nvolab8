import os
class ryu_bgp:
    def create_bgp_speaker(self):
        docker_name = 'ryu'
        cwd = os.getcwd()
        conf_file = cwd+'/ryu_bgp.py'
        try:
            try:
                os.popen('sudo docker stop ' + docker_name).read()
                os.popen('sudo docker rm ' + docker_name).read()
            except: 
                pass
            command = 'sudo docker run -tid -v {}:/root/ryu/ryu/services/protocols/bgp/ryu_bgp.py --ip 172.17.0.3 --name {} ryu-working'.format(conf_file, docker_name)
            os.popen(command).read()
            os.system('sudo docker exec -it ryu ryu-manager ./ryu/ryu/services/protocols/bgp/application.py --bgp-app-config-file ryu/ryu/services/protocols/bgp/ryu_bgp.py')
        except Exception as e:
            print("Error creating sdn controllerx with error {}".format(str(e)))
