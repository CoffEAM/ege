arr = open('txt/26_17687.txt').readlines()
arr = [int(i) for i in arr[1:]]
arr1 = sorted(arr, reverse=True)
print(arr1)
ans1_itog = 0
for i in arr1:
    if (arr1.index(i)+1)%9!=0: # ----- заменить 3 на 9
        ans1_itog += i

besp = arr1[:len(arr1)//9]
ans2_itog = sum(arr1) - sum(besp)
print(ans1_itog, ans2_itog)



