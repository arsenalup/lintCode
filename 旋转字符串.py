给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)
class Solution():
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
        if len(s)==0:
            return s
        elif offset==0  :
            return s[:]
        else:
            offset=offset%len(s)
            s[:]=(s[-offset:]+s[0:-offset])
            