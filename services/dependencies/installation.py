# Controller to handle installing required dependencies and packages on host system
import json
from pathlib import Path

from git import Repo
import subprocess
import apt
import logging

logger = logging.getLogger()

class InstallManager:
    def __init__(self, bootstrap=False):
        # Load project repository if this is new node
        if bootstrap:
            with open('config.json', 'r') as infile:
                config = json.load(infile)
            target = Path(config['bootstrap_dir'])
            Repo.clone_from(config['repository'], target)
            target = target.joinpath('data/packages.json')
            self.install_packages(path=target)
            
    def install_packages(self, packages=None, path=None):
        installation = {}
        if not packages and not path:
            raise Exception('Neither packages nor packages file were specified for installation')
        
        if path:
            with open(path, 'r') as infile:
                new = json.load(path)
                installation.update(new)
        
        # Manually specified packages have priority over package file
        if packages:
            if not isinstance(packages, list) and not isinstance(packages, dict):
                raise Exception('Packages provided are not a list or dictionary')
            installation.update({'manual': packages})
        
        cache = self.update_and_open_cache()
        for package in installation:
            pkg = cache[package]
            if pkg.is_installed:
                logger.info(f'{package} already installed, skipping')
            else:
                pkg.mark_install()

        try:
            cache.commit()
        except Exception as e:
            logger.error('Packages failed to install because of the following;\n' + str(e))
            raise e    
    
    def update_and_open_cache(self):
        cache = apt.cache.Cache()
        cache.update()
        cache.open()
        return cache