from ipaddress import ip_network

network = ip_network('115.192.0.0/255.192.0.0', False)
cnt = 0
for i in network:
    i = str(i).split('.')
    i = list(map(bin, list(map(int, i))))
    i = ''.join(i)
    if i.count('1')%3!=0:
        cnt += 1
print(cnt)


