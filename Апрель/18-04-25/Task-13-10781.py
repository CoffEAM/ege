from ipaddress import ip_address, ip_network

ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')
for mask in range(33):
    net = ip_network(f'112.117.105.64/{mask}', False)
    if ip1 not in (net.broadcast_address, net.network_address):
        if ip2 not in(net.broadcast_address, net.network_address):
            if ip1 in net and ip2 in net:
                print(net.num_addresses)
