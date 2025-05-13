with open('txt/24_9753.txt') as file:
    st = file.readline()

st = st.split('Y')
maax = 0
for i in range(len(st) - 150):
    maax = max(maax, len('Y'.join(st[i:i+151])))
print(maax)
