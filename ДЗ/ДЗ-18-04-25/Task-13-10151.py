from ipaddress import ip_network, ip_address

ip_adres = ip_address('111.81.208.27')
net_adres = ip_address('111.81.192.0')
for mask in range(33):
    net = ip_network(f'111.81.192.0/{mask}', False)
    if net.broadcast_address != ip_adres and ip_adres in net and \
         net.network_address == net_adres:
        print(net.netmask)
