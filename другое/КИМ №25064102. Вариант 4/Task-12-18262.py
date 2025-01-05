for n in range(1, 10000):
    st = '>' + 17*'0' + n*'3' + 17*'2'
    while '>3' in st or '>2' in st or '>0' in st:
        st = st.replace('>3', '22>', 1)
        st = st.replace('>2', '2>', 1)
        st = st.replace('>0', '3>', 1)
    summ = sum(map(int, st[:-1]))
    if int(summ**0.5) == summ**0.5:
        print(n, summ)
        break

