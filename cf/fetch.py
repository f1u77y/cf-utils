import os.path

import lxml.html
import requests

import cf.util


def fetch_tests(rnum):
    if not os.path.exists('tests'):
        os.mkdir('tests')
    base_url = 'http://codeforces.com/contest/{rnum}/problem/{task}'
    problems_count = cf.util.get_problems_count(rnum)
    for task in (chr(i + ord('A')) for i in range(problems_count)):
        print('Task {task}'.format(**locals()))
        url = base_url.format(**locals())
        doc = lxml.html.document_fromstring(requests.get(url).text)
        input_selector = 'div[class=sample-test] div[class=input] pre'
        output_selector = 'div[class=sample-test] div[class=output] pre'

        for i, elem in enumerate(doc.cssselect(input_selector)):
            input_file_name = 'tests/{task}.in.{i}'.format(**locals())
            with open(input_file_name, 'w') as input_file:
                for line in elem.itertext():
                    print(line, file=input_file)

        for i, elem in enumerate(doc.cssselect(output_selector)):
            output_file_name = 'tests/{task}.out.{i}'.format(**locals())
            with open(output_file_name, 'w') as output_file:
                for line in elem.itertext():
                    print(line, file=output_file)


def fetch_problems(rnum):
    base_url = 'http://codeforces.com/contest/{rnum}/problems'
    url = base_url.format(**locals())
    r = requests.get(url).text
    with open('problems.html', 'w') as problems_file:
        print(r, file=problems_file)


def run(args):
    if args.what == 'tests':
        fetch_tests(cf.util.get_round())
    elif args.what == 'problems':
        fetch_problems(cf.util.get_round())


def parse_args(parser):
    parser.add_argument('what', choices=['tests', 'problems'], metavar='WHAT')
    parser.set_defaults(run=run)


__all__ = ['parse_args']
