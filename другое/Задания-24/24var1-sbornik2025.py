with open('txt-24-sbornik2025/24var01.txt') as file:
    st = file.readline()

print(st[342:421])
st = '0++4200-12-32-2--3+0-04+3031-1+21+-310+-0410+310+31---4124423-000044+3-40+100+241-'

st = st.replace('--', ' ').replace('++', ' ')
st = st.replace('+-', ' ').replace('-+', ' ')
st = st.replace(' -', ' ').replace(' +', ' ')
st = st.replace('- ', ' ').replace('+ ', ' ')
st = st.replace('-0-', ' ').replace('-0+', ' ').replace('+0+', ' ').replace('+0-', ' ')
st = st.replace('+0', ' ').replace('-0', ' ')
st = st.replace(' 0', ' ')
st = [i.replace('-', ' ').replace('+', ' ').split() for i in st.split()]

print(st)





