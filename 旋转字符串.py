����һ���ַ�����һ��ƫ����������ƫ������ת�ַ���(����������ת)
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
            