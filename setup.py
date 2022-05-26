import setuptools
setuptools.setup(
      name='cmmsimplesearch',
      version='1.0.0',
      description='CEU Mass Mediator Tool',
      url='https://github.com/diegogomezca/CMM_SimpleSearch',
      author='Diego Gomez',
      install_requires=['requests'],
      scripts=['simplesearch/simpleSearch.py'],
      entry_points={'console_scripts': ['cmmsimplesearch=simplesearch.cli.main']},
)