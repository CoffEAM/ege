from ipaddress import ip_address, ip_network

for mask in range(16, 25):
    net = ip_network(f'127.63.67.1/{mask}', False)
    cnt = 0
    for ip in net:
        ip = f'{int(ip):032b}'
        if ip[:16].count('1') >= ip[16:].count('1'):
            cnt += 1
    if cnt == net.num_addresses:
        print(2**(mask - 16))
        break
