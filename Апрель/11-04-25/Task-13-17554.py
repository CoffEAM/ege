from ipaddress import ip_network

net = ip_network('112.160.0.0/255.240.0.0', False)
ans = 0
for ip in net:
    ip = f'{int(ip)}:032b'
    if ip.count('1') % 3 != 0:
        ans += 1
print(ans)
