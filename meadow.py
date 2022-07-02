import argparse

import api
import services.dependencies.prerequisite as prerequisite
import services.dependencies.installation as installation
import services.provisioning.booting as booting


parser = argparse.ArgumentParser()
parser.add_argument('bootstrap', help='Run node in Docker for provisioning new members')
parser.add_argument('--pxe', help='Start up PXE server for booting nodes without OS')
parser.add_argument('--proxy_dhcp', help='Use proxy DHCP configuration for existing DHCP server')

args = parser.parse_args()
arguments = vars(args)

# Check prerequisites are installed or install them
missing = prerequisite.find_missing()
prerequisite.install(missing)

installMgr = installation.InstallManager(bootstrap=args.bootstrap)
provisioningMgr = booting.BootingManager(arguments)
api.start()
