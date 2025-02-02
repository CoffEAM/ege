from itertools import permutations
from string import digits, ascii_uppercase

alph = digits + ascii_uppercase
cnt = 0
for val in permutations(alph[:12], 6):
    val = ''.join(val)
    cnt_chet = sum(1 for i in val if int(i, 12) % 2 == 0)
    cnt_nech = sum(1 for i in val if int(i, 12) % 2 == 1)
    if val[0] != '0' and val.count('B') == 1 and cnt_chet == cnt_nech:
        cnt += 1
print(cnt)
