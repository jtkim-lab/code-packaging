# Code Packaging and Release

## Installation

Please install the following packages:

```shell
$ pip install numpy
$ pip install pytest
$ pip install pylint
$ pip install black
```

or install them with a single line:

```shell
$ pip install -r requirements.txt
```

## Linear Regression

A simple linear model can be defined as follows:

$$y = {\boldsymbol \theta}^\top \mathbf{x}.$$

Given $n$ data points and their corresponding noisy evaluations,
you can calculate a closed-form solution of ${\boldsymbol \theta}$ solving least squares:

$${\boldsymbol \theta} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y},$$

where $\mathbf{X} \in \mathbb{R}^{n \times d}$ and $\mathbf{y} \in \mathbb{R}^n$.

## Code Refactoring

An example is located in `src/linear_regression_bad_style.py`.

1. Rename variables.
2. Make code simple.
3. Add assertions.
4. Run `pylint`.
5. Run `black`.
6. Add unit tests.

## Documentation

Run `sphinx-build -M html . .` in the `docs` directory.
