cimport sockio

def get_SIOCGIFNETMASK():
	return sockio.SIOCGIFNETMASK

def get_SIOCGIFADDR():
	return sockio.SIOCGIFADDR

def get_SIOCGIFBRDADDR():
	return sockio.SIOCGIFBRDADDR