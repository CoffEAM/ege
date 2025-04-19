from ipaddress import ip_network, ip_address

'''1'''
# ip1 = ip_address('112.117.107.70')
# ip2 = ip_address('112.117.121.80')
# for mask in range(33):
#     net = ip_network(f'112.117.105.64/{mask}', False)
#     if ip1 in net and ip2 in net and ip1 != net.broadcast_address and ip2 != net.broadcast_address:
#         print(net.netmask)

'''2'''
ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')
for mask in range(33):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1.network_address == net2.network_address:
        if ip1 not in (net1.network_address, net1.broadcast_address):
            if ip2 not in (net2.network_address, net2.broadcast_address):
                print(net1.netmask)
