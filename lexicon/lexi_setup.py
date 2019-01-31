try:
    from setuptools import setup, find_packages
except ImportError:
    from disutils.core import setup


config = {
    'description': 'Making a Scanner and Parser',
    'author': 'John Desmond',
    'url': 'https:github.com/yohn-dezmon/yohn-dezmon-hard-way',
    'download_url': 'https:github.com/yohn-dezmon/yohn-dezmon-hard-way',
    'author_email': 'johndesmond631@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['modules'],
    'scripts': [],
    'name': 'ex49'
}

setup(**config)
