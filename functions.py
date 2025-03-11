'''Все делители числа'''
def f(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)


'''Перевод систем счислений'''
from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]


'''Шаблон к типу-1 Задание-24'''
with open('input.txt') as file:
    st = file.readline()

st = st.replace('CD', 'C*D')  # Замена требуемой последовательности
st = st.split('*')
ans = 0
for i in range(len(st) - 161):  # 161 при требуемых 160
    ans = max(ans, len(''.join(st[i:i + 161])))


'''16е задание без setrecursionlimit'''
from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 11:
        return n
    else:
        return n + f(n-1)

for i in range(10, 2025):
    f(i)

print(f(2024) - f(2021))

'''Задание 23'''
def f(current, end):
    if current == end:
        return 1
    if current > end:
        return 0
    return f(current + 2, end) + f(current + 1, end) + f(current*2, end)

print(f(7, 10))
