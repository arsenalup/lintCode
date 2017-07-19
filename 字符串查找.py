class Solution:
    def strStr(self, source, target):

        if target == '':
            return 0
            # write your code here
        elif target not in source or source == None:
            return -1

        else:
            for i in range(0, len(source)):
                if source[i:i + len(target)] == target:
                    return i