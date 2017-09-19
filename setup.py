"""Sets up the armcalcsvc module.
"""

from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.md")) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="armcalcsvc",
    version="1.1.1",
    description="Python client for ArmCalc web service",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/WSDOT-GIS/armcalc-svc-py/",
    author="Washington State Department of Transportation",
    license="Public Domain",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Software Development :: Libraries",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
    keywords="armcalc webservice rest",
    packages=find_packages(),
    install_requires=[]
)
