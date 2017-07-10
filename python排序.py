# """快排"""
# def qsort(seq):
#     if seq == []:
#         return seq
#     else:
#         pivot = seq[0]
#         lesser = qsort([a for a in seq[1:] if a<pivot])
#         greater = qsort([a for a in seq[1:] if a>=pivot])
#         return lesser + [pivot] + greater
#



"""冒泡排序"""

def bubblesort(seq):
    for i in range(len(seq)-1):
        for j in range(len(seq)-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq


if __name__ == '__main__':
    seq = [5, 6, 78, 9, 0, -1, 2, 2, 3, -65, 12]
    print(bubblesort(seq))