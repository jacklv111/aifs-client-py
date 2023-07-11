"""
    Aifs api

    aifs api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import configparser

from setuptools import find_packages, setup  # noqa: H301


def __get_install_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        reqs = [x.strip() for x in f.read().splitlines()]
    reqs = [x for x in reqs if not x.startswith("#")]
    return reqs

config = configparser.ConfigParser()
config.read('setup.cfg')

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

setup(
    name=config['metadata']['name'],
    version=config['metadata']['version'],
    description="Aifs api",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Aifs api"],
    python_requires=">=3.6",
    data_files=[
        ("requirements", ["requirements.txt"]),
        ('setup.cfg', ['setup.cfg'])
    ],
    install_requires=__get_install_requirements(),
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    aifs api  # noqa: E501
    """
)
