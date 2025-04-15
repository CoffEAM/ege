from ipaddress import ip_network

for a in range(256):
    net = ip_network(f'248.112.{a}.35/255.255.255.240', False)
    lennet = 0
    cnt = 0
    for ip in net:
        lennet += 1
        ip = f'{int(ip):032b}'
        if ip[:16].count('0') <= ip[16:].count('0'):
            cnt += 1
    if cnt == lennet:
        print(a)
