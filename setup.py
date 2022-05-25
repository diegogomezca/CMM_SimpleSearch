import setuptools
setuptools.setup(
      name='cmmsimplesearch',
      version='1.0.0',
      description='CEU Mass Mediator Tool',
      url='https://github.com/diegogomezca/CMM_SimpleSearch',
      author='Diego Gomez',
      entry_points={'console_scripts': ['cmmsimplesearch=src.cli:main']},
      packages=setuptools.find_packages(where="src"),
)