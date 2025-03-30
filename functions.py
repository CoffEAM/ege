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

'''Задание 19-21'''
def f(x, s):
    if x >= 40: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 1, s - 1), f(x + 4, s - 1), f(x * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 40) if f(s, 2)])
print('20)', [s for s in range(1, 40) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(1, 40) if f(s, 4) and not f(s, 2)])

