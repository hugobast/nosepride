try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="nosepride",
    author="Hugo Bastien",
    author_email="hugobast@gmail.com",
    url="https://github.com/hugobast/nosepride.git",
    version="0.1.0",
    packages=[
        "nosepride",
        "nosepride/formatters",
        "nosepride/utils"
    ],
    tests_require=["mock"],
    install_requires=[
        "nose",
        "setuptools"
    ],
    test_suite='tests',
    license="MIT License",
    description="Fabulous colors for nosetests",
    long_description=open("README.txt").read(),
    entry_points = {
        'nose.plugins.0.10': [
            'nosepride = nosepride:Nosepride'
        ]
    }
)
