ans = 0
for n in range(1, 101):
    st = '1' + n * '0'
    while '10' in st or '1' in st:
        if '10' in st:
            st = st.replace('10', '0001', 1)
        elif '1' in st:
            st = st.replace('1', '0', 1)
    if len(st) % 7 == 0:
        ans += 1
print(ans)
