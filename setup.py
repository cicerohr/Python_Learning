import os

from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='Python Learning',
    version='',
    packages=[''],
    url='',
    license='MIT License',
    author='CHR',
    author_email='your_email@domain.com',
    description='The objective of this project is to create programs for '
                'learning the Python programming language, as well as the use '
                'of libraries to improve the performance of algorithms.',
    long_description=read('README.md'),
)
