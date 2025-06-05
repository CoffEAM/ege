maxx = 0
for n in range(4, 10000):
    st = '3' + n * '5'
    while '333' in st or '555' in st:
        if '555' in st:
            st = st.replace('555', '3', 1)
        else:
            st = st.replace('333', '5', 1)
    maxx = max(maxx, sum(map(int, st)))
print(maxx)
