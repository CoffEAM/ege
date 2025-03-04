from ipaddress import ip_network

net = ip_network('142.108.56.118/255.255.255.240', False)

for ip in net:
    if bin(int(ip))[-16:].count('1') > bin(int(ip))[:-16].count('1'):
        print(ip)


