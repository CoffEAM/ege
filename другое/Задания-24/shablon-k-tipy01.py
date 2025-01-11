with open('input.txt') as file:
    data = file.readline()

data = data.replace('CD', 'C*D')
data = data.split('*')

ans = 0
for i in range(len(data) - 161):
    ans = max(ans, len(''.join(data[i:i+161])))

print(ans)

