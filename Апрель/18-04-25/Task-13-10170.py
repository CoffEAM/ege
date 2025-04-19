from ipaddress import ip_address, ip_network

ip1 = ip_address('193.175.175.231')
ip2 = ip_address('193.175.176.118')
for mask in range(33):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1 != net2:
        print(mask)

print(int('11110000', 2))
