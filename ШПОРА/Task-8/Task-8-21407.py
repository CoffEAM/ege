from itertools import product

ans = 0
for i in product('ДГИАШЭ', repeat=5):
    i = ''.join(i)
    if i[0] not in 'ИАЭ' and i[-1] not in 'ДГШ':
        ans += 1
print(ans)
