# python3 setup_util.py build_ext --inplace

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("util.pyx")
)