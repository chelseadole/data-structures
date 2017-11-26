"""Setup module for Chelsea's data structures."""

from setuptools import setup

setup(
    name='Data structures',
    description='Various data structures in python',
    author='Chelsea Dole',
    author_email='chelseadole@gmail',
    package_dir={' ': 'src'},
    py_modules=['bst'],
    install_requires=[],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']})
