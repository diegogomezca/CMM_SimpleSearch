from setuptools import setup, find_packages


setuptools.setup(name='cmmsimplesearch',
      version='1.0.0',
      description='CEU Mass Mediator Tool',
      url='https://github.com/diegogomezca/CMM_SimpleSearch',
      author='Diego Gomez',
      packages=setuptools.find_packages(where="src")
)