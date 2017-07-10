def conflict(state, nextx):
    nexty = len(state)
    for i in range(nexty):
        #保证x坐标不相等，x.y的差值不想等即不在一条直线上
        if abs(state[i] - nextx) in (0, nexty - i):
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos, )
            else:
                for result in queens(num, state + (pos, )):
                    yield (pos, ) + result


list1 = list(queens())
print(list1)