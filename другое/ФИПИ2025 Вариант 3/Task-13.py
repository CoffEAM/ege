from ipaddress import ip_network

net = ip_network('210.66.110.0/255.255.252.0', False)

cnt = 0
for ip in net:
    ipv = ''
    for i in str(ip).split('.'):
        ipv += bin(int(i))[2:]
    if ipv.count('1')%6!=0:
        cnt += 1
print(cnt)
#934

