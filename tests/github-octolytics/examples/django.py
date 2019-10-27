import github_octolytics

url = 'https://github.com/django/django'
octolytics = github_octolytics.get(url)
print(octolytics)
