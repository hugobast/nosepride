from distutils.core import setup

setup(
    name="nosepride",
    author="Hugo Bastien",
    author_email="hugobast@gmail.com",
    url="",
    version="0.0.1",
    packages=["nosepride"],
    install_requires=["nose"],
    license="MIT License",
    long_description=open("README.txt").read(),
    entry_points = {
        'nose.plugins.0.10': [
            'nosepride = nosepride:Nosepride'
        ]
    }
)
