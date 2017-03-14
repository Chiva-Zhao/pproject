prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
print(min(prices), max(prices))
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
print(sorted(zip(prices.values(), prices.keys())))

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
# print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

print(min(prices, key=lambda k: prices[k]))  # Returns 'FB'
print(max(prices, key=lambda k: prices[k]))  # Returns 'AAPL'
min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)