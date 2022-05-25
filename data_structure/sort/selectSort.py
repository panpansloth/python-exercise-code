# 选择排序在冒泡排序的基础上做了改进，每次遍历列表的时候，只做一次交换。
# 要实现这一点，选择排序在遍历时寻找最大值，并在遍历完之后将它放在正确位置上
def selectSort(alist):
    for i in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for j in range(1, i + 1):
            if alist[j] > alist[positionOfMax]:
                positionOfMax = j
        alist[i], alist[positionOfMax] = alist[positionOfMax], alist[i]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectSort(alist)
print(alist)
