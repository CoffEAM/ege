from ipaddress import ip_network

for A in range(256):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', False)
    cnt = 0
    for ip in net:
        ip = bin(int(''.join(str(ip).split('.'))))[2:]
        if ip.count('1') > 15:
            cnt += 1
    if cnt == len(list(net)):
        print(A)
        break


