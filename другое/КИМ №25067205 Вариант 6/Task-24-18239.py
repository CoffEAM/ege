with open('txt/24_18239.txt') as file:
    st = file.readline()
st = [int(i) for i in st.split('-') if i != '']
res = 0
lenn = 0
ans = []
for num in st:
    res -= num
    lenn += len(str(num)) + 1
    if res < -20000:
        ans.append(lenn-(len(str(num))+1))
        res = 0
        lenn = 0
print(max(ans))
