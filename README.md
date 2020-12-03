<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/github-octolytics.svg?maxAge=3600)](https://pypi.org/project/github-octolytics/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/github-octolytics.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/github-octolytics.py/actions)

### Installation
```bash
$ [sudo] pip install github-octolytics
```

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
    <a href="https://readme42.com/">readme42.com</a>
</p>
