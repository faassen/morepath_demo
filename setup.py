import os
from setuptools import setup, find_packages

setup(name='mpdemo',
      version = '0.1dev',
      description="Morepath demo app",
      author="Martijn Faassen",
      author_email="faassen@startifact.com",
      license="BSD",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'morepath',
        'waitress',
        ],
      extras_require = dict(
        test=['pytest >= 2.0',
              'pytest-cov'],
        ),
      entry_points= {
        'console_scripts': [
            'mpdemo = mpdemo.app:main',
            ]
        },
      )
