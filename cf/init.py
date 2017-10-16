import shutil
from cf.config import global_conf, global_conf_dir


def make_new_workdir(round_num, tasks_num):
    round_skeleton_dir = f'{global_conf_dir}/round-skeleton/'
    shutil.copytree(round_skeleton_dir, round_num)
    ext = global_conf['all.extension']
    skeleton_filename = f'{global_conf_dir}/file-skeletons/skeleton.{ext}'
    for i in range(tasks_num):
        task = chr(ord('a') + i)
        shutil.copy(skeleton_filename, f'{round_num}/{task}.{ext}')


def parse_args(argv):
    make_new_workdir(argv[1], int(argv[2]))


__all__ = ['parse_args']
