from ipaddress import ip_network, ip_address

ip1 = ip_address('211.115.61.154')
ip2 = ip_address('211.115.59.137')
for mask in range(33):
    net = ip_network(f'211.115.57.136/{mask}', False)
    if ip1 in net and ip2 in net and \
        ip1 != net.broadcast_address and ip2 != net.broadcast_address:
            print(net.netmask)
