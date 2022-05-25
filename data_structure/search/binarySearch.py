# 对于有序列表来说，二分搜索算法在最坏情况下的时间复杂度O(logn)
# 有序列表的二分搜索
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while not found and first < last:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        elif alist[midpoint] > item:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return found


alist = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
found = binarySearch(alist, 5)
print(found)


# 二分搜索的递归版本
def binarySearch1(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        elif alist[midpoint] > item:
            return binarySearch1(alist[:midpoint], item)
        else:
            return binarySearch1(alist[midpoint + 1:], item)


alist = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
found = binarySearch1(alist, 77)
print(found)
