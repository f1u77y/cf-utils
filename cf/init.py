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


def run(args):
    make_new_workdir(args.round_num, args.tasks_num)


def parse_args(parser):
    parser.add_argument('round_num', metavar='ROUND-NUMBER')
    parser.add_argument('tasks_num', metavar='TASKS-NUMBER', type=int)
    parser.set_defaults(run=run)


__all__ = ['parse_args']
