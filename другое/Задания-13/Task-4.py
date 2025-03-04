from ipaddress import ip_network

for a in range(9):
    A = int('1'*a + '0'*(8-a), 2)
    net = ip_network(f'199.59.129.3/255.255.{A}.0', False)
    if all(bin(int(ip))[:-16].count('1')>=bin(int(ip))[-16:].count('1') for ip in net):
        print(A)
