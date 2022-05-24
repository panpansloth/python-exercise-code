# 问题：我们想去除序列中出现的重复元素，但是仍然保持剩下的元素顺序不变
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

