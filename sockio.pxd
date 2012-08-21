cdef extern from 'sys/ioctl.h':
	pass

cdef extern from 'arpa/inet.h':
	pass

cdef extern from 'net/if.h':
	unsigned int SIOCGIFNETMASK
	unsigned int SIOCGIFADDR
	unsigned int SIOCGIFBRDADDR
