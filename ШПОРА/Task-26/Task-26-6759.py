with open('txt/26_6759.txt') as file:
    n = int(file.readline())
    prices = sorted([int(i) for i in file], reverse=True)

ans1 = sum(prices[i] for i in range(n) if (i + 1) % 3 != 0)
prices = prices[::-1]
ans2 = sum(prices[n//3:])
print(ans1, ans2)
