from ipaddress import ip_network, ip_address

for a in range(256):
    net_ip = f'127.63.{67&a}.0'
    try:
        net = ip_network(f'{net_ip}/255.255.{a}.0', False)
        cnt = 0
        for ip in net:
            ip = f'{int(ip):032b}'
            if ip[:16].count('1') >= ip[16:].count('1'):
                cnt += 1
        if cnt == net.num_addresses:
            print(a)
    except:
        continue

