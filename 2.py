# 设计一个算法，计算出n阶乘中尾部零的个数
# 计算量过大超时
import math
class Solution:
    # @param n a integer
    # @return as a integer
    def trailingZeros(self, n):
        c = math.factorial(n)
        a = []
        a.extend(str(c))
        b = 0
        for i in a[::-1]:
            if int(i) == 0:
                b += 1
            elif int(i) != 0:
                break
        return b
