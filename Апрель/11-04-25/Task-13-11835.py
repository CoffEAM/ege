from ipaddress import ip_network

cnt = 0
for a in range(256):
    net = ip_network(f'207.0.{a}.167/255.255.255.192', False)
    for ip in net:
        lcnt = f'{int(ip):032b}'[:16].count('0')
        rcnt = f'{int(ip):032b}'[16:].count('0')
        if not (lcnt > rcnt):
            break
    else:
        cnt += 1
print(cnt)
