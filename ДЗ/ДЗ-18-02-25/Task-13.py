from ipaddress import ip_network

net = ip_network('101.157.240.0/255.255.252.0', False)

ans = 0
for ip in net:
    ip = str(ip).split('.')
    ip_r = ''.join([bin(int(i))[2:] for i in ip[:2]])
    ip_l = ''.join([bin(int(i))[2:] for i in ip[2:]])
    if ip_r.count('1')>ip_l.count('1'):
        ans += 1
print(ans)
