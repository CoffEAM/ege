with open('txt/17_5882.txt') as file:
    data = [int(i) for i in file]

ans = []
for i in range(len(data) - 1):
    para = data[i:i+2]
    u = sum(1 for k in para if str(k)[-1] == '3')
    if u == 1:
        ans.append(min(para))

u = sum(int(i)**2 for i in str(abs(min(ans))))
ans = []
for i in data:
    if '3' in str(i) and i >= u:
        ans.append(i)
print(len(ans), min(ans))
