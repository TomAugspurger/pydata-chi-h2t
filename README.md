# Pandas .head() to .tail()

<a rel="license" href="http://creativecommons.org/licenses/by/3.0/us/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/3.0/us/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/us/">Creative Commons Attribution 3.0 United States License</a>

Materials for the pandas tutorial at PyData Chicago 2016.

# Setup

Change directory into the tutorial repo:

```
$ cd pydata-chi-h2t
```

And proceed with the installation, depending on whether you're using conda or pip.

## Conda / Miniconda

Create a new environment using the provided `environment.yml`

```
$ conda env create
```

This will make a new environment called `ph2t`.
Once it's created, make sure to run `source activate ph2t` or `activate ph2t`
(depending on your platform) to activate it.

Check the install with

```
$ python check_environment.py
```

Then run

```
$ jupyter notebook
```

and open the first notebook `1-Basics.ipynb`.


## Pip / virtualenv

Hopefully you know what you're doing.
I believe the current recommended way of creating virtualenvs is either

```
$ pyvenv /path/to/new/virtual/environment
```

or

```
$ python3 -m venv myenv
```

Make sure that you're creating a python3 environment. The notebooks should
mostly work with python2, but no promises.
If you call the environment `ph2t`, then activate it and install the requirements.

```
$ source /path/to/ph2t/bin/activate
$ python -m pip install -r requirments.txt
```

Check the install with

```
$ python check_environment.py
```

Then run

```
$ jupyter notebook
```

and open the first notebook `1-Basics.ipynb`.

# Notebooks

1. [Basics](1-Basics.ipynb)
2. [Operations](2-Operations.ipynb)
3. [Indexing](3-Indexing.ipynb)
4. [Groupby and Reshaping](4-GroupbyAndReshaping.ipynb)
5. [Tidy Data](5-TidyData.ipynb)
6. [For Stats & ML](6-StatsAndML.ipynb)

# Further Resources

- Wes McKinney's [*Python for Data Analysis*](http://shop.oreilly.com/product/0636920023784.do)
- [The official docs](http://pandas.pydata.org/pandas-docs/stable/)
- [Brandon Rhodes PyCon Tutorial](https://github.com/brandon-rhodes/pycon-pandas-tutorial)
- Joris Van den Bossche's [Introductory Tutorial](https://github.com/jorisvandenbossche/pandas-tutorial)
- My [series of articles](https://github.com/tomaugspurger/modern-pandas)
