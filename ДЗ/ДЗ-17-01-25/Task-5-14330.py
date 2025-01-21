for n in range(10000, 100000):
    ksum = (max(map(int, str(n))) + min(map(int, str(n))))**2
    arr = [int(i) for i in str(n) if int(i)%2==0]
    psum = 1
    for i in arr:
        psum *= i
    r = str(max(ksum, psum)) + str(min(ksum, psum))
    if r == '12116':
        print(n)
        break

