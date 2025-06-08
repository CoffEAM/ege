with open('txt/26_4629.txt') as file:
    n = int(file.readline())
    products = sorted([int(i) for i in file], reverse=True)

ans1 = sum(products[:n//4])//2 + sum(products[n//4:])
products = products[::-1]
ans2 = sum(products[:n//4])//2 + sum(products[n//4:])
print(ans1, ans2)
