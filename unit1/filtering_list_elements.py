# 问题：序列中含有一些数据，我们需要提取其中的值或者根据某些标准对序列做删减
# 筛选序列中的数据，通常最简单的方法是使用列表推导（list comprehension）
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# All positive values
pos = [n for n in mylist if n > 0]
# All negative values
neg = [n for n in mylist if n < 0]

print('pos:', pos)
print('neg:', neg)

# Negative values clipped to 0
neg_clip = [n if n > 0 else 0 for n in mylist]
# Positive values clipped to 0
pos_clip = [n if n < 0 else 0 for n in mylist]
print('pos_clip:', pos_clip)
print('neg_clip:', neg_clip)
