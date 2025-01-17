st = open('imaev/24_stat22_mart.txt').readline()
from string import ascii_uppercase

for i in ascii_uppercase:
    if i != 'D' and i != 'C':
        st = st.replace(i, '-')
st = st.replace('D', 'D D')
st = st.split()
arr = [i for i in st if i.count('C')>=2 and len(i)>9]
print(len(arr))

#10518 правильно


