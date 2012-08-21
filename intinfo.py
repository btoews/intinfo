import fcntl,socket,struct
import ioctl_requests
import array

def get_ip(iface):
    request = ioctl_requests.get_SIOCGIFADDR()  
    addr = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), request, struct.pack('256s', iface[:15]))[20:24])
    return addr

def get_mask(iface):
    request = ioctl_requests.get_SIOCGIFNETMASK()
    mask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), request, struct.pack('256s', iface[:15]))[20:24])
    return mask

def get_broadcast(iface):
    request = ioctl_requests.get_SIOCGIFBRDADDR()
    addr = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), request, struct.pack('256s', iface[:15]))[20:24])
    return addr

# from http://code.activestate.com/recipes/439093-get-names-of-all-up-network-interfaces-linux-only/?in=user-2551140
def get_interfaces(): 
    request = ioctl_requests.get_SIOCGIFCONF()
    max_possible = 128  # arbitrary. raise if needed.
    bytes = max_possible * 32
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    names = array.array('B', '\0' * bytes)
    outbytes = struct.unpack('iL', fcntl.ioctl(
        s.fileno(),
        request,
        struct.pack('iL', bytes, names.buffer_info()[0])
    ))[0]
    namestr = names.tostring()
    return [namestr[i:i+32].split('\0', 1)[0] for i in range(0, outbytes, 32)]
