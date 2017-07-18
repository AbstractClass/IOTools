import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='iotools',
    packages=['iotools'],
    version='0.4',
    description='A wrapper for simple file IO to eliminate boilerplate.',
    author='Connor MacLeod',
    author_email='connor.macleod96@hotmail.ca',
    url='https://github.com/AbstractClass/IOTools/',
    download_url='https://github.com/AbstractClass/IOTools/archive/0.4.tar.gz',
    keywords=['file', 'IO', 'csv', 'json'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    ]
)