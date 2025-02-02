for num in range(770000, -1000000, -1):
    summ_del = 0
    cnt_del = 0
    for delitel in range(1, num//2):
        if num%delitel==0:
            summ_del += delitel
            cnt_del += 1
    A = int(summ_del/cnt_del)
    if str(A)[-2:]=='12':
        print(num, A)

