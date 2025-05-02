from ipaddress import ip_address, ip_network

net = ip_network('102.141.0.0/255.255.192.0')
ans = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 7 == 0 and ip[-4:] == '1011':
        ans += 1
print(ans)
