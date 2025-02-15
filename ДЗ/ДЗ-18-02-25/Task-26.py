with open('txt/26.txt') as file:
    N = file.readline()
    fights = [list(map(int, i.split())) for i in file]

fights = sorted(fights)
fights = [[sum(i), *i] for i in fights]
print(sorted(fights))


# ans = 0
# for i in range(len(fights)):
#     start, time, end = fights[i]
#     collected = []
#     for k in fights[i:]:
#         if end <= k[0]:
#             start, time, end = k
#             collected.append(k)
#     if len(collected) > ans:
#         ans = len(collected)
# print(ans)

