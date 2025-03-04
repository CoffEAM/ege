from ipaddress import ip_network

for A in range(17):
    net = ip_network(f'255.211.33.160/{16 + A}', False)
    if all(bin(int(ip))[:-16].count('1')>=bin(int(ip))[-16:].count('1') for ip in net):
        print(int(f'{A*'1'}0000', 2))
        break
