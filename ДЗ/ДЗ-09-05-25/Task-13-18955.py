from ipaddress import ip_network, ip_address

ip1 = ip_address('200.154.190.12')
ip2 = ip_address('200.154.184.0')
for mask in range(33):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1 == net2:
        if ip1 not in [net1.network_address, net1.broadcast_address]:
            if ip2 not in [net2.network_address, net1.broadcast_address]:
                if ip1 in net2 and ip2 in net1:
                    print(mask)
