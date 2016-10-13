"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

REQUIREMENTS = ['google-cloud==0.20.0',
                'psycopg2',
                'google-api-python-client==1.5.3']

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ebmdatalab-python',
    version='0.0.5',
    description='Tools used by EBMDataLab when interacting with BigQuery',
    long_description=long_description,
    url='https://github.com/ebmdatalab-tools',
    author='Seb Bacon',
    author_email='tech@ebmdatalab.net',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='bigquery utilities',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': ['check-manifest', 'mock'],
    },
)
