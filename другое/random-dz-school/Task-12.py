st = '5' * 72
while '333' in st or '555' in st:
    if '555' in st:
        st = st.replace('555', '3', 1)
    else:
        st = st.replace('333', '5', 1)
print(st)
