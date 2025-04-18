from ipaddress import ip_network, ip_address

ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')
for mask in range(33):
    net = ip_network(f'112.117.105.64/{mask}', False)
    if ip1 in net and ip2 in net and ip1 != net.broadcast_address and ip2 != net.broadcast_address:
        print(net.netmask)
