with open('txt/26_4660.txt') as file:
    n = int(file.readline())
    products = sorted([int(i) for i in file], reverse=True)

ans1 = sum(products[i] for i in range(n) if (i + 1) % 4 == 0)//2 + sum(products[i] for i in range(n) if (i + 1) % 4 != 0)
products = products[::-1]
ans2 = sum(products[:n//4])//2 + sum(products[n//4:])
print(ans1, ans2)
