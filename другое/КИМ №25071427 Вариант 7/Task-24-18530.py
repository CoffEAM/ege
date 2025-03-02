with open('txt/24_18530.txt') as file:
    st = file.readline()

for i in 'AE':
    st = st.replace(i, '*')

for i in 'BCDFGH':
    st = st.replace(i, '-')

st = st.split('*')
arr = []
for i in st:
    if i != '':
        arr.append(i)

ar_pr = []
ans = []
for i in range(len(arr) - 2):
    tr = arr[i:i+3]
    for k in range(1, 101):
        if (len(tr[0]) == len(tr[1]) + k == len(tr[2]) + 2*k) \
            or (len(tr[0]) == len(tr[1]) - k == len(tr[2]) - 2*k):
            ar_pr.append(tr)
        else:
            if len(ar_pr) > 1:
                if ar_pr[-1] != ['']:
                    ar_pr.append([''])

port = []
for i in ar_pr:
    lenn = sum(len(k) for k in i)
    if lenn!=0:
        port.append(lenn)
x = max(ar_pr, key=lambda x: x[-1])

print(port)
zxcv = []
yui = []
for i in range(len(port) - 1):
    for k in range(1, 30):
        if port[i] + k == port[i+1]:
            yui.append(port[i])
        else:
            yui.append(port[i])
            if yui != []:
                zxcv.append(yui)
            yui.clear()
print(zxcv[:100])


