from ipaddress import ip_network

for a in range(16, 25):
    net = ip_network(f'152.65.245.132/{a}', False)
    for ip in net:
        lcnt = f'{int(ip):032b}'[:16].count('0')
        rcnt = f'{int(ip):032b}'[16:].count('0')
        if not (lcnt >= rcnt):
            break
    else:
        print(net.netmask)
