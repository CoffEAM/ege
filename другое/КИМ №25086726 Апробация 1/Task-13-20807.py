from ipaddress import ip_network

net = ip_network('172.16.192.0/255.255.192.0')
ans = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 5 != 0:
        ans += 1
print(ans)
