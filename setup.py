import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Flask-Geckoboard',
    description='Geckoboard custom widgets for Flask projects',
    packages=[
        'flask_geckoboard',
        'tests',
    ],
    install_requires=(
        'flask'
    ),
    extras_require={
        'encryption': ['pycrypto']
    },
    keywords=['flask', 'geckoboard'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
    url='http://github.com/neocortex/flask-geckoboard',
    download_url='http://github.com/neocortex/flask-geckoboard/archives/master',
)
