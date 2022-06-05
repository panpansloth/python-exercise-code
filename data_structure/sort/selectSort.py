"""
selectSort概念：
首先，找到数组中最小的那个元素，
其次，将它和数组的第一个元素交换位置（如果第一个元素就是最小元素那么它就和自己交换）。
再次，在剩下的元素中找到最小的元素，将它与数组的第二个元素交换位置。
如此往复，直到将整个数组排序。
这种方法叫做选择排序，因为它在不断地选择剩余元素之中的最小者。
"""


def selectSort(alist):
    for i in range(len(alist) - 1):
        positionOfMin = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[positionOfMin]:
                positionOfMin = j
        alist[i], alist[positionOfMin] = alist[positionOfMin], alist[i]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectSort(alist)
print(alist)
