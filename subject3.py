# 给定一个只包含字母的字符串，返回单个字母出现的次数
# 考察字典的概念和使用
# 返回值为包含元组的列表，格式如下（对列表中元组的顺序不做要求）
# 参数 "hello"
# 返回值 [('h', 1), ('e', 1), ('l', 2), ('o', 1)]


def letter_count(str):
    dir = {}

    for i in str:
        if i in dir:
            dir[i] += 1
        else:
            dir[i] = 1

    return dir.items()


print(letter_count('hello'))
