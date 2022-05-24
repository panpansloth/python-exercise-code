# 问题：我们想在字典上对数据执行各式各样的计算（比如求最小值、最大值和排序等）
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Find min price
min_price = min(zip(prices.values(), prices.keys()))
# Find max price
max_price = max(zip(prices.values(), prices.keys()))
print('min price:', min_price)
print('max_price:', max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()), reverse=True)
print('sorted prices:', prices_sorted)
