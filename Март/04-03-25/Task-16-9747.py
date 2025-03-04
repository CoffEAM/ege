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
