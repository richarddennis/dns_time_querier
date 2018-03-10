import socket
import time
import urllib2

hostname = 'stackoverflow.com'

dns_start = time.time()
ip_address = socket.gethostbyname(hostname)
dns_end = time.time()

url = 'https://%s/' % ip_address
req = urllib2.Request(url)
req.add_header('Host', hostname)

handshake_start = time.time()
stream = urllib2.urlopen(req)
handshake_end = time.time()

data_start = time.time()
data_length = len(stream.read())
data_end = time.time()

print 'DNS time            = %.2f ms' % ((dns_end - dns_start) * 1000)
print 'HTTP handshake time = %.2f ms' % ((handshake_end - handshake_start) * 1000)
print 'HTTP data time      = %.2f ms' % ((data_end - data_start) * 1000)
print 'Data received       = %d bytes' % data_length
