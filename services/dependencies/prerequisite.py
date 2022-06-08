import os
import sys
import json
import subprocess

def get_packages(package_file='data/packages.json'):
    with open(package_file, 'r') as infile:
        packages = json.load(infile)
        packages = packages['prerequisite']
    return packages

def install_prerequisites(packages):
    subprocess.call(['sudo', 'apt', 'update'])
    subprocess.call(['sudo', 'apt', 'install', *packages, '-y'])
    # Restart script with same arguments
    os.execv(sys.argv[0], sys.argv)

def check():
    packages = get_packages()
    for package in packages:
        out = subprocess.call(f'dpkg -s {package}')
        # TODO: Ensure this actually works to check package is installed
        if not out:
            return False
    return True