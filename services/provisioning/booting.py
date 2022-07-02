from pypxe import dhcp, http
import netifaces

class ProvisioningManager:
    def __init__(self, bootstrap=False):
        if bootstrap:
            self.start_pxe_server()
    
    def start_pxe_server(self):
        ifaces = netifaces.interfaces()
        addresses = []
        for inf in ifaces:
            definition = netifaces.ifaddresses(inf)
            ipv4_addresses = definition[netifaces.AF_LINK]
            for ipv4 in ipv4_addresses:
                addresses.extend(ipv4)
    
        # TODO: Decide address to use from 'addresses' based on configuration options
        dhcp.DHCPD({'ip': '192.168.'})
        http.HTTPD()

    def establish_ssh(self):
        pass