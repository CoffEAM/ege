from ipaddress import ip_network

for bit in range(9):
    net = ip_network(f'238.51.1.202/{16 + bit}', False)
    cnt = 0
    for ip in net:
        ip = f'{int(ip):032b}'
        if ip[:16].count('1') >= ip[16:].count('1'):
            cnt += 1
    if cnt == net.num_addresses:
        print(int(f'{bit*'1'}00', 2))
        break
