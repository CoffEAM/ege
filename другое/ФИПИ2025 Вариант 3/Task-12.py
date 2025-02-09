st = 2025*'1'
while '1111' in st or '5555' in st:
    if '1111' in st:
        st = st.replace('1111', '55', 1)
    else:
        st = st.replace('5555', '5', 1)
print(st)
#51
