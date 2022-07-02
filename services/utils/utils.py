import os
import sys


def restart_script():
    # Restart script with same arguments
    os.execv(sys.argv[0], sys.argv)
