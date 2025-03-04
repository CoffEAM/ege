from ipaddress import ip_network

net = ip_network('252.67.33.87/255.252.0.0', False)

cnt = 0
for ip in net:
    prav = bin(int(ip))[-16:].count('1')
    lev = bin(int(ip))[:-16].count('1')
    if prav > lev * 2:
        cnt += 1
print(cnt)
