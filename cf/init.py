import shutil

from cf.config import global_conf, global_conf_dir
import cf.util


def make_new_workdir(round_num, problems_num):
    round_skeleton_dir = f'{global_conf_dir}/round-skeleton/'
    shutil.copytree(round_skeleton_dir, round_num)
    ext = global_conf['all.extension']
    skeleton_filename = f'{global_conf_dir}/file-skeletons/skeleton.{ext}'
    for i in range(problems_num):
        task = chr(ord('a') + i)
        shutil.copy(skeleton_filename, f'{round_num}/{task}.{ext}')


def run(args):
    problems_num = args.problems_num
    if problems_num == -1:
        problems_num = cf.util.get_problems_count(args.round_num)
    make_new_workdir(args.round_num, problems_num)


def parse_args(parser):
    parser.add_argument('round_num', metavar='ROUND-NUMBER')
    parser.add_argument('problems_num', metavar='PROBLEMS-NUMBER', type=int, nargs='?', default=-1)
    parser.set_defaults(run=run)


__all__ = ['parse_args']
