# python3 setup.py build_ext --inplace

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("module_cython.pyx")
)