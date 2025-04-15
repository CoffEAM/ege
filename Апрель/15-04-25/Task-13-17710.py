from ipaddress import ip_network

net = ip_network('214.187.224.0/255.255.224.0')
ans = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip[-4:] == '1000' and ip.count('1') % 6 != 0:
        ans += 1
print(ans)
