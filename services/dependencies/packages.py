import json


class PackageManager:
    def __init__(self, package_file='data/packages.json'):
        with open(package_file, 'r') as infile:
            self.packages = json.load(infile)

    def get_section(self, section):
        return self.packages[section]


pkgMgr = PackageManager()
