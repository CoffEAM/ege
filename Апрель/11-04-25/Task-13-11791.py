from ipaddress import ip_network

for a in range(16, 25):
    net = ip_network(f'246.51.128.202/{a}', False)
    for ip in net:
        lcnt = f'{int(ip):032b}'[:16].count('0')
        rcnt = f'{int(ip):032b}'[16:].count('0')
        if not (lcnt <= rcnt):
            break
    else:
        print(net.netmask)
