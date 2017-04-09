# gdxread

Python package to read gdx data into pandas dataframes

[Install](#install) | [Use](#use) | [Update](#update) | [Uninstall](#uninstall)

## Install

### Dependencies

- Python 2.7 (easiest to get through Anaconda at https://www.continuum.io/downloads)
- pandas (should come automatically with Anaconda)
- GAMS Python bindings: On command line, navigate to the GAMS Python API files for Python 2.7, e.g. C:\GAMS\win64\24.7\apifiles\Python\api, and run this command:
  ```bash
  python setup.py install
  ```
  This will make available the *gdxcc* and *gams* python modules, which are imported by gdxread.

### Get the Latest Package
From command line:
```bash
pip install git+https://github.com/mmowers/gdxread.git@master
```

## Use

To get a pandas dataframe from GDX parameter in a python script:

```python
import gdxread

df = gdxread.get_df_from_param('path_to_gdx_file', 'param_name')
```

## Update

To update/upgrade gdxread, go to command line and enter:

```bash
pip install git+https://github.com/mmowers/gdxread.git@master --upgrade
```

## Uninstall

```
pip uninstall gdxread
```