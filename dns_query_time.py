import socket
import time
import urllib2
import time
import datetime


hostname_array = [ 'dnsseed.bitcoin.dashjr.org', 'seed.bitcoinstats.com', 'seed.bitcoin.jonasschnelli.ch', 'seed.btc.petertodd.org']
while len(hostname_array)>0:
    print "Array not empty"
    hostname = hostname_array[0]
    print hostname
    dns_start = time.time()
    ip_address = socket.gethostbyname(hostname)
    print ip_address
    dns_end = time.time()

    url = 'https://%s/' % ip_address
    req = urllib2.Request(url)
    req.add_header('Host', hostname)

    handshake_start = time.time()
    stream = urllib2.urlopen(req)
    handshake_end = time.time()

    data_start = time.time()
    data_length = len(stream.read())
    data_received = stream.read()
    data_end = time.time()

    print 'Date / time' + str(datetime.datetime.now())
    print 'Hostname            = '+  string(hostname_array[0])
    print 'DNS time            = %.2f ms' % ((dns_end - dns_start) * 1000)
    print 'HTTP handshake time = %.2f ms' % ((handshake_end - handshake_start) * 1000)
    print 'HTTP data time      = %.2f ms' % ((data_end - data_start) * 1000)
    print 'Data received       = %d bytes' % data_length

    path_to_file_coinbase = "dns_query.json"
    with open(path_to_file_coinbase,"a+") as f:
        f.write('{"Hostname": "' + string(hostname_array[0]) + '", "DNS time": "' + str(((dns_end - dns_start) * 1000))+
        '", "HTTP handshake time": "' + str(((handshake_end - handshake_start) * 1000))+
        '", "HTTP data time": "' + str(((data_end - data_start) * 1000))+
        '", "Data received": "' + str(( data_length))
        +'"}\n')

        #TODO STORE DATA RECIEVED BETTER


    #           {"Name": "node-n07.pool-101-108.dynamic.totbb.net", "alias": "[]", "addresslist": "['101.108.116.119']"}


# hostname = 'stackoverflow.com'
#
# dns_start = time.time()
# ip_address = socket.gethostbyname(hostname)
# dns_end = time.time()
#
# url = 'https://%s/' % ip_address
# req = urllib2.Request(url)
# req.add_header('Host', hostname)
#
# handshake_start = time.time()
# stream = urllib2.urlopen(req)
# handshake_end = time.time()
#
# data_start = time.time()
# data_length = len(stream.read())
# data_received = stream.read()
# data_end = time.time()
#
# #print 'Hostname            = '+  string(hostname_array[0])
# print 'DNS time            = %.2f ms' % ((dns_end - dns_start) * 1000)
# print 'HTTP handshake time = %.2f ms' % ((handshake_end - handshake_start) * 1000)
# print 'HTTP data time      = %.2f ms' % ((data_end - data_start) * 1000)
# print 'Data received       = %d bytes' % data_length
