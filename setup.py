#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='simplemona',
      version='0.6.0',
      description='Monacoin mining with no registration required.',
      author='Musee Ullah (original: Eric Cook)',
      author_email='milkteafuzz@gmail.com',
      url='http://simplemona.com',
      entry_points={
          'console_scripts': [
              'sm_rpc = simplecoin.rpc:entry'
          ]
      },
      packages=find_packages()
      )
