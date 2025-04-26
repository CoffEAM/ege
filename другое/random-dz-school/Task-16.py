def F(n):
    if n < 5:
        return F(n + 1) + \
            F(n + 2) + \
            F(n + 3)
    else:
        return n
print(F(2))
