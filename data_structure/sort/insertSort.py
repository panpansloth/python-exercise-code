# 插入排序原理稍微有不同。它在列表较低的一端维护一个有序的子列表，并逐个将每个新元素‘插入’这个子列表。
# 首先假设位置0处的元素只是单个元素的有序子列表。从元素1到元素n-1，每一轮都将当前元素与有序子列表中的元素进行比较
# 在有序子列表中，将比它大的元素右移；当遇到一个比它小的元素或者抵达子列表终点时，就可以插入当前元素。
def insertSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = currentvalue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertSort(alist)
print(alist)
