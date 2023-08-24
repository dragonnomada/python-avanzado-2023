# python3 -m pip install cython
# python3 setup.py build_ext --inplace

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("sum_of_squares.pyx")
)
