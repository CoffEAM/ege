with open('txt/Txt-24-4602.txt') as file:
    st = file.readline()

st = st.replace('A', '*').replace('O','*')
st = st.replace('B', '-').replace('C', '-').replace('D', '-')

st = st.replace('-*', '#')
st = st.replace('*', ' ').replace('-', ' ')
st = st.split()
print(len(max(st, key=len)))





