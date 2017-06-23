# 给定一个字符串，用以下规则检查合法性
# 完全符合返回 True，否则返回 False
# 1，第一位是字母
# 2，只能包含字母、数字、下划线
# 3，只能字母或数字结尾
# 4，最小长度2
# 5，最大长度10


def valid_password(pwd):
    if ( len(pwd) > 2 and len(pwd) < 10) and pwd[0].isalpha() and (pwd[-1].isalpha() or pwd[-1].isdigits):
        for i in pwd[1:-1]:
            if i.isalpha() or i.isdigit() or (i is '_'):
                return True
        else:
            return False
    else:
        return False

