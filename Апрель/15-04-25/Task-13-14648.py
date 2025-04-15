from ipaddress import ip_network, ip_address

ans = 0
ip = ip_address('218.48.192.56')
net_ip = ip_address('218.48.192.0')
for a in range(9):
    net = ip_network(f'218.48.192.0/{16 + a}', False)
    if net.num_addresses >= 502 and ip in net and net_ip == net.network_address and \
            ip != net_ip and ip != net.broadcast_address:
        ans += 1
print(ans)
