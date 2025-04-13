with open('txt/24_19149.txt') as file:
    st = file.readline()

while '++' in st or '(+' in st or '+)' in st or ')(' in st or '()' in st:
    st = st.replace('++', ' ').replace('(+', ' ').replace('+)', ' ').replace(')(', ' ').replace('()', ' ')

while '+ ' in st or ' +' in st:
    st = st.replace('+ ', ' ').replace(' +', ' ')

for i in '1234':
    st = st.replace(f'){i}', f') {i}').replace(f'{i}(', f'{i} (')

arr = []
for i in st.split():
    if i.count('(') == i.count(')'):
        try:
            u = eval(i) % 2 == 0
            if u:
                arr.append(i)
        except:
            continue
print(len(max(arr, key=len)))
