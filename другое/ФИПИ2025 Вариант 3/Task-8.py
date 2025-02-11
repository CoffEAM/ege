from itertools import product

alph = '123456'

cnt = 0
for num in product(alph, repeat=4):
    num = ''.join(num)
    if num.count('3')==1:
        cnt_chet = sum(1 for i in num if int(i)%2==0)
        cnt_nech = sum(1 for i in num if int(i)%2==1)
        if cnt_chet<=cnt_nech:
            cnt += 1
print(cnt)
#392


