arr = open('txt/26_4660.txt').readlines()

prices = sorted([int(i) for i in arr[1:]])

every_4 = sum([prices[i] for i in range(0, len(prices), 4)])
client = sum(prices) - every_4 + every_4 / 2
store_price = sum(prices[::-1][:7500]) + sum(prices[:2500])/2

print(client, store_price)
