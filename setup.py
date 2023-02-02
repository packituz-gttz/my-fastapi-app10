"""Setup file for application."""
from setuptools import find_packages, setup
from version import __version__

setup(
    name='hello_world',
    version=__version__,
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Fastapi']
)
