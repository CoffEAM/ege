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
