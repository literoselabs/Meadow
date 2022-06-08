import services.dependencies.prerequisite as prerequisite

# Check prerequisites are installed or install them
check = prerequisite.check()
if not check:
    prerequisite.install_prerequisites()

import api
api.start()