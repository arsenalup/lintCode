# 给定一个英文句子（一个只有字母的字符串），将句中所有单词变为有且只有首字母大写的形式


def cap_string(str):
    str = ' '.join([i[0].upper() + i[1:] for i in str.split()])
    return str
