for n in range(1, 10000):
    st = '>' + 21*'0' + n*'1' + 11*'2'
    while '>1' in st or '>2' in st or '>0' in st:
        st = st.replace('>1', '22>', 1)
        st = st.replace('>2', '2>', 1)
        st = st.replace('>0', '1>', 1)
    summ = sum(map(int, st[:-1]))
    if summ%n==0:
        print(n)

