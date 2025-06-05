num = 2 * 729**333 + 2 * 243**334 - 81**335 + 2 * 27**336 - 2 * 9**337 - 338
res = ''
while num:
    res += str(num%9)
    num //= 9
print(len(res) - res.count('0'))
