from fnmatch import fnmatch


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


for i in range(315670, 10 ** 7):
    if fnmatch(str(i), '31*567?') and is_prime(i):
        p = eval('*'.join(list(str(i))))
        print(i, p)
