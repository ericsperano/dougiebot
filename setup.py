#!/bin/env python3
"""
setup
"""
from setuptools import setup

setup(name='dougiebot',
      version='1.0.0',
      description='Dougie Jones Slack Bot',
      url='http://github.com/ericsperano/dougiebot.git',
      author='Eric Sperano',
      author_email='eric.sperano@gmail.com',
      license='MIT',
      packages=['dougiebot'],
      package_data={
          '': ['*.json']
      },
      install_requires=[
          "slackclient"
      ],
      setup_requires=[
          'pytest-runner',
          #'pytest-pylint'
      ],
      tests_require=[
          'pytest',
          #'pylint'
      ],
      entry_points={
          'console_scripts': [
              'dougiebot=dougiebot:main',
          ],
      },
      test_suite="tests",
      zip_safe=False)
