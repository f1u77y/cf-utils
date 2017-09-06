import cf.util
import cf.config
import shutil
import os.path


def make_new_workdir(round_num):
    round_skeleton_dir = f'~/.config/codeforces/round-skeleton/'
    round_skeleton_dir = os.path.expanduser(round_skeleton_dir)
    shutil.copytree(round_skeleton_dir, round_num)
    ext = cf.config.global_conf['all.extension']
    skeleton_filename = f'~/.config/codeforces/file-skeletons/skeleton.{ext}'
    skeleton_filename = os.path.expanduser(skeleton_filename)
    for task in 'abcde':
        shutil.copy(skeleton_filename, f'{round_num}/{task}.{ext}')


def parse_args(argv):
    make_new_workdir(argv[1])


__all__ = ['parse_args']
