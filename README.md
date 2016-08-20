# Pandas .head() to .tail()

[http://git.io/ph2t-chi](http://git.io/ph2t-chi)

[![Join the chat at https://gitter.im/pydata-chi-h2t/Lobby](https://badges.gitter.im/pydata-chi-h2t/Lobby.svg)](https://gitter.im/pydata-chi-h2t/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Materials for the pandas tutorial at PyData Chicago 2016.
Please run either the conda or pip setup below before the session.

# Setup

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

