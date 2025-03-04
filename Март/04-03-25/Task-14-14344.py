for p in range(16, 37):
    num = int('17496', p) + int('91F83', p) + int('D9543', p)
    if num%12==0:
        print(num//12)
