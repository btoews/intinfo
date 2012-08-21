intinfo
=======

Portable (between *nixes) information about network interfaces

## Description ##

There is no good cross-platform way to get interface info in python. This doesn't solve that problem, but it at least allows for cross-*nix distro access to this data. 

Values for `SIOCGIFADDR`,`SIOCGIFNETMASK`, and `SIOCGIFBRDADDR` were different between my Linux and OSX boxes. I don't know if there are differences beyond that.

Implemented here is a simple Cython module that sucks in these magic values from the apropriate headers and makes them accessible to Python.

## Usage ##

    import intinfo
    print intinfo.get_ip('eth1')
    print intinfo.get_mask('eth1')
    print intinfo.get_broadcast('eth1')

## Intstallation ##

You should be able to just:

    sudo python ./setup.py install


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