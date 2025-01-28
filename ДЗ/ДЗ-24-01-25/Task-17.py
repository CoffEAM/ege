arr = open('txt/17_8562.txt').readlines()
arrr = [int(i) for i in arr]
arr = [[int(arr[i]), int(arr[i + 1])] for i in range(len(arr) - 1)]
spisok = [i for i in range(-10, 11)]
minn = min(i for i in arrr if (-100) < i < 100 and i not in spisok) ** 2

ans = 0
summ = []
for i in arr:
    if i[0] ** 2 < minn < i[1] ** 2 or i[0] ** 2 > minn > i[1] ** 2:
        if sum(i) >= 0:
            ans += 1
            summ.append(sum(i))

print(ans, min(summ))
print(minn)
