# 合并两个排序的整数数组A和B变成一个新的数组。

class Solution():
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self,A, B):
        # write your code here
        A.extend(B)
        A.sort()
        return A

A=[1,2,3]
B=[2]
a=Solution()
a.mergeSortedArray(A,B)
print(A)