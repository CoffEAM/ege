from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

with open('txt-Krilov-2025/24var04.txt') as file:
    st = file.readline()

while '--' in st or '**' in st or '*-' in st or '-*' in st:
    for i in ['--', '**', '*-', '-*']:
        st = st.replace(i, ' ')

while ' *' in st or ' -' in st or '- ' in st or '* ' in st:
    for i in [' *', ' -', '- ', '* ']:
        st = st.replace(i, ' ')

for k in alph[:16]:
    while f' 0{k}' in st or f'-0{k}' in st or f'*0{k}' in st:
        for i in [f' 0{k}', f'-0{k}', f'*0{k}']:
            st = st.replace(i, f' {k}')

print(len(max(st.split(), key=len)))
