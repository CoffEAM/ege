from ipaddress import ip_network

net = ip_network('222.121.128.0/255.255.224.0', False)
cnt = 0
for ip in net:
    ip = str(ip)
    ip = ip.split('.')
    ip = '.'.join(bin(int(i))[2:] for i in ip)
    if ip[-2]==ip[-1]:
        cnt += 1
print(cnt)
