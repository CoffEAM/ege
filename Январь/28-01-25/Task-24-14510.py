from dataclasses import replace
from string import ascii_uppercase
st = open('txt/24_14510.txt').readline()
gl = 'AEIOUY'
sogl = [i for i in ascii_uppercase if i not in gl]
for i in gl:
    st = st.replace(i, '+')
for i in sogl:
    st = st.replace(i, '-')
st = st.replace('--+', '#')
print(st[:200])
st = st.split('#')
cnt_len = 100000
for i in range(len(st)-498):
    lene = '--+'.join(st[i:i+499])
    cnt_len = min(cnt_len, len(lene))
print(cnt_len)

