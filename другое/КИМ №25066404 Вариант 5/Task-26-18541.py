arr = open('txt/26_18541.txt').readlines()
N, M = list(map(int, arr[0].split()))
snaryadi = [int(i) for i in arr[1:M]]
maks_arletov = [int(i) for i in arr[-M:]]

snaryadi = sorted(snaryadi, reverse=True)
maks_arletov = sorted(maks_arletov)

selected = []

for atlet in maks_arletov:
    for snaryad in snaryadi:
        if snaryad <= atlet:
            selected.append(snaryad)
            break
print(int(sum(selected)/len(selected)), max(selected, key=lambda x: selected.count(x)))

