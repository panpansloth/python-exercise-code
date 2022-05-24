# 问题：我们有多个字典或映射，想在逻辑上将它们合并未一个单独的映射结构，以此来执行某个特定的操作，比如查找值或者检查键是否存在
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)

print(c['x'])
print(c['y'])
# 如果有重复的键，那么这里会采用第一个映射中所对应的值
print(c['z'])  # 3

# 修改映射的操作，总是会作用在列出的第一个映射结构上
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# del c['y']  # KeyError: "Key not found in the first mapping: 'y'"

# 作为ChainMap的替代方案,我们可能会考虑利用字典update()方法将多个字典合并在一起
# 这个需要单独构建一个完整的字典对象(如果任何一个原始字典做了修改,这个改变都不会反应到合并后的字典中)
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])
a['x'] = 13
print(merged['x'])  # 1

# ChainMap使用的原始字典,因此它不会产生这种令人不悦的行为
merged1 = ChainMap(a, b)
print(merged1['x'])
a['x'] = 42
print(merged['x'])
