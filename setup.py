from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(name='cmmsimplesearch',
      version='1.0.0',
      packages=find_packages(where="src"),
)