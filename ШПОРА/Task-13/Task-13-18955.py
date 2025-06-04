from ipaddress import ip_address, ip_network

ip1 = ip_address('200.154.190.12')
ip2 = ip_address('200.154.184.0')
for mask in range(10, 31):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1 == net2:
        if ip1 in net1.hosts() and ip2 in net1.hosts():
            if ip1 in net2.hosts() and ip2 in net2.hosts():
                print(mask)
