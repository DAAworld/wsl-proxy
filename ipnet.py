import subprocess
import re


class IpNet(object):

    def __init__(self, ports_list) -> None:
        self.ports_list = ports_list

    def del_exist_ports(self):
        all_proxy = subprocess.check_output("netsh interface portproxy show all", shell=True)
        ports = set(re.findall("\d{4}", str(all_proxy)))
        for port in ports:
            subprocess.run(f"netsh interface portproxy delete v4tov4 listenaddress=0.0.0.0 listenport={port}", shell=True)
            print(port)

    def get_wsl_ip(self):
        cv = subprocess.check_output('''bash.exe -c "ifconfig eth0 | grep 'inet'"''', shell=True)
        ip = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", str(cv,'utf-8')).group()
        self.ip = ip

    def show_proxy(self):
            subprocess.run("netsh interface portproxy show all", shell=True)

    def start(self):
        for x in self.ports_list:
            subprocess.run(
                f"netsh interface portproxy add v4tov4 listenport={x} listenaddress=0.0.0.0 connectport={x} connectaddress={self.ip}",
                shell=True)
        print("绑定成功......")
    

if __name__ == "__main__":
    port_list = [80, 443, 8800, 9000, 9002]
    ipnet = IpNet(port_list)
    ipnet.del_exist_ports()
    ipnet.get_wsl_ip()
    ipnet.start()
    ipnet.show_proxy()

