from setuptools import setup

setup(name='gdxread',
      version='0.1',
      description='Functions for reading GAMS gdx data into a pandas dataframe',
      url='http://github.com/mmowers/gdxread',
      author='Matt Mowers',
      author_email='Matthew.Mowers@nrel.gov',
      packages=['gdxread'],
      install_requires=[
          'gams',
          'os',
          'pandas',
          'gdxcc'
      ],
      zip_safe=False)
