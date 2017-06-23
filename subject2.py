# 返回 100 内的素数列表
# 考察基本的循环和选择概念、列表的使用

def prime_numbers():
    a = []
    for i in range(1, 100):
        if i == 1:
            a.append(1)
        else:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                a.append(i)

    return a


print(prime_numbers())
