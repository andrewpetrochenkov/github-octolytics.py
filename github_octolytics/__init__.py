__all__ = ['parse', 'get']

import re

import requests


def getvalue(value):
    if value in ['false', 'true']:
        return 'true' in value
    if value.isdigit():
        return int(value)
    return value


def parse(html):
    """parse a html string and return a dictionary with octolytics data"""
    matches = re.findall(r'<meta\b[^>]*[^/] />', html)
    data = dict()
    for m in matches:
        if 'name="octolytics-' in m:
            values = re.findall('="(.*?)"', m)
            name, value = values[0], getvalue(values[1])
            data[name] = value
    return data


def get(url):
    """make GET request and return a dictionary with octolytics data"""
    r = requests.get(url)
    return parse(r.text)
