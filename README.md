#gdxread

Python package to read gdx data into pandas dataframes

[Install](#install) | [Use](#use) | [Uninstall](#uninstall)

## Install

### Dependencies

- Python 2.7 (easiest to get through Anaconda at https://www.continuum.io/downloads)
- pandas
- GAMS Python bindings, namely gdxcc and gams: On command line, navigate to the GAMS Python API files for Python 2.7, e.g. C:\GAMS\win64\24.7\apifiles\Python\api and run this command:
  ```bash
  python setup.py install
  ```

### Get the Latest Package

```bash
pip install git+https://github.com/mmowers/gdxread.git@master
```

## Use

To get a pandas dataframe from GDX parameter:

```python
import gdxread

df = gdxread.get_df_from_param('/path/to/gdxfile')
```

## Uninstall

```
pip uninstall gdxpds
```