import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(
    name="nosepride",
    author="Hugo Bastien",
    author_email="hugobast@gmail.com",
    url="https://github.com/hugobast/nosepride.git",
    version="0.1.6",
    packages=find_packages(exclude=["tests"]),
    tests_require=["mock", "coverage"],
    install_requires=[
        "nose",
        "setuptools"
    ],
    test_suite='tests',
    license="MIT License",
    description="Fabulous colors for nosetests",
    long_description=open("README.rst").read(),
    entry_points={
        'nose.plugins.0.10': [
            'nosepride = nosepride.nosepride:Nosepride'
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Testing",
        "Environment :: Plugins",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ],
    **extra
)
