from ipaddress import ip_network, ip_address

ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')
for mask in range(32):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1 == net2:
        if ip1 not in [net1.network_address, net1.broadcast_address]:
            if ip2 not in [net2.network_address, net2.broadcast_address]:
                if ip2 in net1 and ip1 in net2:
                    print(net2.num_addresses)
