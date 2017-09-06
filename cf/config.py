import yaml
import os.path


global_conf_path = '~/.config/codeforces/config.yaml'
global_conf_path = os.path.expanduser(global_conf_path)


global_conf = yaml.load(open(global_conf_path))


__all__ = ['global_conf']
