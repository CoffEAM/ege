with open('txt/17_7716.txt') as file:
    arr = [int(i) for i in file]

nech = '02468'

maxx = max([i for i in arr if '0' not in str(i) and '2' not in str(i) and '4' not in str(i) and '6' not in str(i) and '8' not in str(i)])

ans = []
for i in range(len(arr)-1):
    para = arr[i:i+2]
    k1 = [i for i in str(para[0]) if i not in '13579']
    k2 = [i for i in str(para[1]) if i not in '13579']
    if (''.join(k1) == str(para[0]) or ''.join(k2) == str(para[1])) and sum(para) > maxx:
        ans.append(sum(para))
print(len(ans), max(ans))
