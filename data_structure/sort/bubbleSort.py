# 冒泡排序多次遍历列表，它比较相邻的元素，将不合顺序的交换。
# 每一轮遍历都将下一个最大值放到正确的位置上。

def bubbleSort(alist):
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)
