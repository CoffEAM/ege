st = open('imaev/24-s1.txt').readlines()

minn = min(i.count('A') for i in st)
arr = [i for i in st if i.count('A')==minn]
arr = arr[0]
maxx = max([arr.count(i), i] for i in arr)
print(maxx)
print(''.join(st).count('V'))

#38429 - правильно
