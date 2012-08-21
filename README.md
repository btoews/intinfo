intinfo
=======

Portable (between *nixes) information about network interfaces

## Rebuilding Cython Portion ##
To simplify distribution, the setup.py file builds from the `ioctl_requests.c`
rather than `ioctl_requests.pyx`. To re-build the cython module, you could run

    cython ./ioctl_requests.pyx

or you could write a new setup.py like this:

	from distutils.core import setup
	from distutils.extension import Extension
	from Cython.Distutils import build_ext

	ext_modules = [Extension("ioctl_requests", ["ioctl_requests.pyx"])]

	setup(
	  name = 'ioctl_requests',
	  cmdclass = {'build_ext': build_ext},
	  ext_modules = ext_modules
	)