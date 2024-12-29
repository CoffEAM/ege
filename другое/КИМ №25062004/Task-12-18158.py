ans = 0
for n in range(4, 10000):
    st = '4' + '1'*n
    while '411' in st or '1111' in st:
        st = st.replace('411', '14', 1)
        st = st.replace('1111', '1', 1)
    summ = sum(map(int, st))
    if summ > ans:
        ans = summ
print(ans)


