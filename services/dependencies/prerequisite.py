import subprocess

from packages import pkgMgr

from ..utils import utils


def install(required):
    if not required:
        return required
    subprocess.call(['sudo', 'apt', 'update'])
    subprocess.call(['sudo', 'apt', 'install', '-y', *required])

    failed = find_missing(required)
    if not failed:
        utils.restart_script()

    pkgs = ', '.join(failed)
    raise Exception(f'Failed to install the following packages (you may try manually): {pkgs}')


def find_missing(required=None):
    # Get prerequisite section of needed packages
    if not required:
        required = pkgMgr.get_section('prerequisites')
    # Get all installed packages listed
    process = subprocess.Popen(['apt', 'list', '--installed'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stdout = stdout.decode()
    installed = stdout.splitlines()
    installed = [line.split('/')[0] for line in installed]
    # Return packages required but not present
    missing = [package for package in required if package not in installed]
    return missing
