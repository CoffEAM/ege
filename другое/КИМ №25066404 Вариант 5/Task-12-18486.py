cnt = []
for n in range(4, 10000):
    st = '7' + n*'6'
    while '766' in st or '667' in st:
        st = st.replace('766', '67', 1)
        st = st.replace('667', '7', 1)
    cnt.append(st)
print(len(set(cnt)))

