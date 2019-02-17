import os.path

import yaml


global_conf_dir = os.path.expanduser('~/.config/codeforces/')
file_skeletons_dir = f'{global_conf_dir}/file-skeletons/'
global_conf_path = f'{global_conf_dir}/config.yaml'
global_conf = yaml.load(open(global_conf_path))


__all__ = ['global_conf', 'global_conf_dir']
