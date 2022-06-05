"""
分治法:
a. 一个很复杂的事情
b. 分解成若干的小事情
c. 然后重新组合

mergeSort概念:要将一个数组排序，可以先（递归地）将它分成两半分别排序，然后将结果归并起来。
a. 它是递归算法，每次将一个列表一分为二
b. 如果列表为空或只有一个元素，那么从定义上来说它就是有序的（基本情况）,
   如果列表不止一个元素，就将列表一分为二，并对两部分都递归调用归并排序.
c. 当两部分都有序后，就进行归并这一基本操作.
   归并是指将两个较小的有序列表归并为一个有序列表的过程.

mergeSort时间复杂度：
分析mergeSort函数时，要考虑它的两个独立的构成部分。
首先，列表被一分为二。在学习二分搜索时已经算过，当列表的长度为n时，能切分log2n次。
第二个处理过程是归并。列表中的每个元素最终都得到处理，并被放到有序列表中。所以，得到长度为n的列表需要进行n次操作。
由此可知，需要进行logn次拆分，每一次需要进行n次操作，所以一共是nlogn次操作。
也就是说，归并排序算法的时间复杂度是O(nlogn)。
"""


def merge(alist, lefthalf, righthalf):
    """合并两个已经排序好的列表，产生一个新的已排序好的列表"""
    i = 0
    j = 0
    k = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[k] = lefthalf[i]
            i += 1
        else:
            alist[k] = righthalf[j]
            j += 1
        k += 1
    # 拷贝left列表剩余的元素
    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i += 1
        k += 1
    # 拷贝right列表剩余的元素
    while j < len(righthalf):
        alist[k] = righthalf[j]
        j += 1
        k += 1


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(alist, lefthalf, righthalf)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
