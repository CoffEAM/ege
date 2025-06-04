from ipaddress import ip_address, ip_network

ip1 = ip_address('95.24.2.9')
ip2 = ip_address('95.24.3.10')
ans = 0
for mask in range(10, 31):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1.network_address != net2.network_address:
        if ip1 in net1.hosts() and ip2 in net2.hosts():
            cnt1 = 0
            for i in net1.hosts():
                i = f'{int(i):032b}'
                if i[-1] == '0':
                    cnt1 += 1
            cnt2 = (net2.num_addresses - 2) // 2
            ans = max(ans, cnt1, cnt2)
print(ans)
