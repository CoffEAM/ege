from itertools import permutations
from math import factorial

cnt = 0
errors = [''.join(i) for i in permutations('ОУАЮЕ')]
print(factorial(12) - len(errors)*factorial(8))

# for val in permutations('ХОЧУНАБЮДЖЕТ'):
#     val = ''.join(val)
#     for error in errors:
#         if error not in val:
#             cnt += 1
# print(cnt)

