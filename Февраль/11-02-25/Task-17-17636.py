with open('txt/17_17636.txt') as file:
    arr = [int(i) for i in file]

maxx = max(i for i in arr if str(i)[-1]=='3' and 100<=abs(i)<=999)
troiki = [[arr[i], arr[i+1], arr[i+2]] for i in range(len(arr)-2)]
ans = []
for troika in troiki:
    k = sum(1 for i in troika if str(i)[-1]=='3' and 100<=abs(i)<=999)
    if k >= 1 and sum(troika) < maxx:
        ans.append(sum(troika))
print(len(ans), max(ans))
