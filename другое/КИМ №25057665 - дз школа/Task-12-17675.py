st = 134 * '9'
while '22222' in st or '9999' in st:
    if '22222' in st:
        st = st.replace('22222', '99')
    else:
        st = st.replace('9999', '2')
print(st)

