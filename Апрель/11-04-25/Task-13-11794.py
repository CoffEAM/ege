from ipaddress import ip_network

for a in range(256):
    net = ip_network(f'223.167.{a}.167/255.255.255.192', False)
    ans = True
    for ip in net:
        lcnt = f'{int(ip):032b}'[:16].count('0')
        rcnt = f'{int(ip):032b}'[16:].count('0')
        if lcnt > rcnt:
            ans = False
    if ans:
        print(a)
