# 问题：有两个字典，我们想找出它们中间可能相同的地方（相同的键、相同的值等）
# 要找出这两个字典中的相同之处，只需要通过keys()或者items()方法执行常见的集合操作即可
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}
# Find keys in common
print(a.keys() & b.keys())  # {'y', 'x'}
# Find keys in a that not in b
print(a.keys() - b.keys())  # {'z'}
# Find (keys,values) pairs in common
print(a.items() & b.items())  # {('y', 2)}
