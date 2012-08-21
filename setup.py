from distutils.core import setup
from distutils.extension import Extension
#from setuptools import setup
#from setuptools.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("ioctl_requests", ["ioctl_requests.pyx"])]

setup(
  name = 'intinfo',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  py_modules = ['intinfo'],

)