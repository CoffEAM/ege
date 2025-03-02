st = 140*'8'
while '888' in st or '2222' in st:
    if '2222' in st:
        st = st.replace('2222', '88')
    else:
        st = st.replace('888', '22')

print(st)
