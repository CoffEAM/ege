with open('txt/17.txt') as file:
    arr = [int(i) for i in file]

maxx = max([i for i in arr if str(i)[-2:]=='50'])

ans = []
for i in range(len(arr) - 3):
    troika = arr[i:i+3]
    k = [i for i in troika if 10000 <= abs(i) <= 99999]
    if len(set(troika)) == len(troika) and k == troika and sum(troika) <= maxx:
        ans.append(sum(troika))
print(len(ans), max(ans))
