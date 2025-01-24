for x in range(1, 2006):
    num = 43 ** 56 + 113 ** 841 - x
    res = ''
    while num:
        res += str(num%4)
        num //= 4
    chet = sum(1 for i in res if i in '02')
    nech = sum(1 for i in res if i in '13')
    if chet%2==0 and nech%2==0 and res.count('2')<=712:
        print(x)