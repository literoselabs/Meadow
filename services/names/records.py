from copyreg import add_extension
from python_hosts import Hosts, HostsEntry

class NameRecords:
    def __init__(self, hostfile='/etc/hosts'):
        self.hosts = Hosts(path=hostfile)
        self.add_entry('127.0.0.1', ['local', 'localhost'])

    def add_entry(self, address, names):
        entry = HostsEntry(entry_type='ipv4', address=address, names=names)
        self.hosts.add([entry])
        self.hosts.write()