from ipaddress import ip_address, ip_network

ip1 = ip_address('121.171.5.70')
ip2 = ip_address('121.171.5.107')
for mask in range(33):
    net = ip_network(f'121.171.5.66/{mask}', False)
    if ip1 not in (net.broadcast_address, net.network_address):
        if ip2 not in (net.broadcast_address, net.network_address):
            if ip1 in net and ip2 in net:
                print(net.num_addresses)
