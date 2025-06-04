from ipaddress import ip_address, ip_network

net = ip_network('98.81.154.195/255.252.0.0', False)
for ip in net:
    print(''.join(str(ip).split('.')))

