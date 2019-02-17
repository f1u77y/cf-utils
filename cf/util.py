import os

import lxml.html
import requests


def get_round():
    return os.path.basename(os.getcwd())


def get_problems_count(rnum):
    url = f'https://codeforces.com/contest/{rnum}/problems'
    doc = lxml.html.document_fromstring(requests.get(url).text)
    return len(doc.xpath("//div[@class='problem-statement']"))
