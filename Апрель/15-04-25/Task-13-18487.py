from ipaddress import ip_network, ip_address

for a in range(256):
    net_ip = f'192.214.{a}.{184&224}'
    net = ip_network(f'{net_ip}/255.255.255.224', False)
    cnt = 0
    for ip in net:
        ip = f'{int(ip):032b}'
        if ip.count('1') > 15:
            cnt += 1
    if cnt == net.num_addresses:
        print(a)
