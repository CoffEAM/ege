st = open('txt/24var03.txt').readline()

while '*-' in st or '-*' in st or '--' in st or '**' in st:
    st = st.replace('*-', ' ')
    st = st.replace('-*', ' ')
    st = st.replace('--', ' ')
    st = st.replace('**', ' ')

while ' -' in st or ' *' in st or '* ' in st or '- ' in st:
    st = st.replace(' -', ' ').replace(' *', ' ')
    st = st.replace('- ', ' ').replace('* ', ' ')

for i in '0123456789':
    while f'-0{i}' in st or f'*0{i}' in st:
        st = st.replace(f'-0{i}', f' {i}')
        st = st.replace(f'*0{i}', f' {i}')

while ' 0' in st:
    st = st.replace(' 0', ' ')

print(len(max(st.split(), key=len)))

#356

