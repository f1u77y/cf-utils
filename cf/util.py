import os

import lxml.html
import requests


def get_round():
    return os.path.basename(os.getcwd())


def get_problems_count(rnum):
    base_url = 'http://codeforces.com/contest/{rnum}/problems'
    url = base_url.format(**locals())
    r = requests.get(url).text
    doc = lxml.html.document_fromstring(r)
    return len(doc.xpath("//div[@class='problem-statement']"))
