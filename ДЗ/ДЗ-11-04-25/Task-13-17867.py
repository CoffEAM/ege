from ipaddress import ip_network

net = ip_network('172.16.168.0/255.255.248.0', False)
ans = 0
for ip in net:
    ip = bin(int(ip))[2:]
    if ip.count('1') % 5 != 0:
        ans += 1
print(ans)
