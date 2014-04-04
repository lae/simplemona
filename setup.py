#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='simplemona',
      version='0.5.0',
      description='Monacoin mining with no registration required.',
      author='Eric Cook/Musee Ullah',
      author_email='milkteafuzz@gmail.com',
      url='http://simplemona.com',
      entry_points={
          'console_scripts': [
              'sm_rpc = simplecoin.rpc:entry'
              'sc_rpc = simplecoin.rpc:entry'
          ]
      },
      packages=find_packages()
      )
