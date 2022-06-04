"""在分析quickSort函数时要注意，
对于长度为n的列表，如果分区操作总是发生在列表的中部，就会切分logn次。
为了找到分割点，n 个元素都要与基准值比较。所以，时间复杂度是O(nlogn)。
另外，快速排序算法不需要像归并排序算法那样使用额外的存储空间。
"""
def quickSort(alist, first, last):
    # 如果列表长度大于1，则进行分区操作并递归的排序
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSort(alist, first, splitpoint - 1)
        quickSort(alist, splitpoint + 1, last)


# 第二步：分区操作，首先找到两个坐标---leftmark和rightmark，他们分别位于列表剩余元素的开头和末尾
# 分区的目的是根据待排序元素与基准值的相对大小，将它们放到正确的一边，同时逐步逼近分割点
def partition(alist, first, last):
    """第一步：选出一个基准值。基准值的作用是帮助切分列表。在最终的有序列表中，基准值的位置通常被称为分割点。"""
    # 算法在分割点切分列表，以进行对快速排序的子调用。
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    while True:
        # 首先加大leftmark，直到遇到一个大于基准值的元素
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        # 然后减少rightmark，直到遇到一个小于基准值的元素
        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1
        # 当rightmark小于left时候，过程终止，此时rightmark的位置就是分割点
        if leftmark > rightmark:
            break
        # 找到两个与最终分割点错序的元素，互换这两个元素的位置，然后重复上述过程
        alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    # 将基准值与当前分割点的位置互换，即可使基准值位于正确位置
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist, 0, len(alist) - 1)
print(alist)
