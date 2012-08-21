cdef extern from 'sys/ioctl.h':
	pass

cdef extern from 'arpa/inet.h':
	pass

cdef extern from 'net/if.h':
	pass

cdef extern from 'sys/sockio.h':
	unsigned int SIOCGIFNETMASK
	unsigned int SIOCGIFADDR
	unsigned int SIOCGIFBRDADDR