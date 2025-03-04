from ipaddress import ip_network

for a in range(256):
    net = ip_network(f'127.254.{a}.10/255.255.224.0', False)
    if all(bin(int(ip))[:-16].count('1') >= bin(int(ip))[-16:].count('1') for ip in net):
        print(a)
