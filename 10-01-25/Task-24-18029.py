with open('Txt-24-18029.txt') as file:
    st = file.readline()

st = st.replace('Y', '*')
st = st.replace('X', 'X X')
st = st.replace('XX', ' ')
st = st.split()

maxx = max(i.count('*') for i in st)
print(max(len(i) for i in st if i.count('X')==2 and i.count('*')==maxx))



