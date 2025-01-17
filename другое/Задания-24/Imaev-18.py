st = open('imaev/24_23osn.txt').readline()
from string import digits, ascii_uppercase
alph = digits+ascii_uppercase

for i in alph[19:]:
    st = st.replace(i, ' ')
st = st.split()
print(len(max(st, key=len)))



