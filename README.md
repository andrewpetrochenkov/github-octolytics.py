<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/github-octolytics.svg?longCache=True)](https://pypi.org/project/github-octolytics/)
[![](https://img.shields.io/pypi/v/github-octolytics.svg?maxAge=3600)](https://pypi.org/project/github-octolytics/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/github-octolytics.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/github-octolytics.py/)

#### Installation
```bash
$ [sudo] pip install github-octolytics
```

#### Functions
function|`__doc__`
-|-
`github_octolytics.get(url)` |make GET request and return a dictionary with octolytics data
`github_octolytics.parse(html)` |parse a html string and return a dictionary with octolytics data

#### Examples
```python
>>> import github_octolytics
>>> github_octolytics.get('https://github.com/django/django')
{'octolytics-host': 'collector.githubapp.com', 'octolytics-app-id': 'github', 'octolytics-event-url': 'https://collector.githubapp.com/github-external/browser_event', 'octolytics-dimension-request_id': '6C86:1AB6A:1553F2A:20148E0:5DB5986A', 'octolytics-dimension-region_edge': 'ams', 'octolytics-dimension-region_render': 'iad', 'octolytics-dimension-ga_id': '', 'octolytics-dimension-visitor_id': 6848789782742800491, 'octolytics-dimension-user_id': 27804, 'octolytics-dimension-user_login': 'django', 'octolytics-dimension-repository_id': 4164482, 'octolytics-dimension-repository_nwo': 'django/django', 'octolytics-dimension-repository_public': True, 'octolytics-dimension-repository_is_fork': False, 'octolytics-dimension-repository_network_root_id': 4164482, 'octolytics-dimension-repository_network_root_nwo': 'django/django', 'octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown': False}

```

```python
>>> import requests
>>> r = requests.get('https://github.com/django/django')
>>> github_octolytics.parse(r.text)
{...}
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>