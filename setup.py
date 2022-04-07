from setuptools import setup, find_packages

setup(
    name='countlines',
    packages=find_packages(include=['countlines']),
    version='1.0.0',
    description='CountLines - Command line tool that counts your project\'s lines, and other cool features',
    author='Nawaf and Khayal',
    license='MIT',
    keywords=['countlines', 'lines', 'words', 'lines counter', 'count'],
    setup_requires=['fire', 'prettytable']
)