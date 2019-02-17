import logging
import os.path
from urllib.request import urlretrieve

import lxml.html
import requests

import cf.util


log = logging.getLogger(__name__)


def fetch_tests(rnum):
    if not os.path.exists('tests'):
        os.mkdir('tests')
    problems_count = cf.util.get_problems_count(rnum)
    for task in (chr(i + ord('A')) for i in range(problems_count)):
        log.info('Fetching task {task}...', task=task)
        url = f'https://codeforces.com/contest/{rnum}/problem/{task}'
        doc = lxml.html.document_fromstring(requests.get(url).text)
        input_selector = 'div[class=sample-test] div[class=input] pre'
        output_selector = 'div[class=sample-test] div[class=output] pre'

        for i, elem in enumerate(doc.cssselect(input_selector)):
            with open(f'tests/{task}.in.{i}', 'w') as input_file:
                for line in elem.itertext():
                    print(line, file=input_file)

        for i, elem in enumerate(doc.cssselect(output_selector)):
            with open(f'test/{task}.out.{i}', 'w') as output_file:
                for line in elem.itertext():
                    print(line, file=output_file)


def fetch_problems(rnum):
    urlretrieve(f'https://codeforces.com/contest/{rnum}/problems', 'problems.html')


def run(args):
    if args.what == 'tests':
        fetch_tests(cf.util.get_round())
    elif args.what == 'problems':
        fetch_problems(cf.util.get_round())


def parse_args(parser):
    parser.add_argument('what', choices=['tests', 'problems'], metavar='WHAT')
    parser.set_defaults(run=run)


__all__ = ['parse_args']
