from setuptools import setup, find_packages
import os

VERSION = '0.0.1'
DESCRIPTION = 'Package to read COLVAR file'
LONG_DESCRIPTION = 'A package that allows you to read COLVAR output from Plumed and access data'

# Setting up
setup(
    name="colvar",
    version=VERSION,
    author="sbhakat (Soumendranath Bhakat)",
    author_email="<bhakatsoumendranath@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'pandas'],
    keywords=['python', 'COLVAR', 'Plumed'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
    ]
)
