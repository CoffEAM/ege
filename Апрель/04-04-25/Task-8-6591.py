from itertools import product

ans = 0
for num in product('0123456', repeat=5):
    num = ''.join(num)
    s_chet = sum(int(i) for i in num if i in '0246')
    s_nech = sum(int(i) for i in num if i in '135')
    if num[0] != '0' and num.count('6') == 1 and s_chet < s_nech:
        ans += 1
print(ans)
