import itertools


def print_matrix(w, h, x=0, y=0):
    #确定初始坐标
    op = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    #四个旋转方向
    direction = itertools.cycle(op)
    result = {(xx, yy): None for xx in range(w) for yy in range(h)}
    result[(x, y)] = 1
    _x, _y = next(direction)
    #2.3用法有差别
    i = 1
    flag = 0
    #四次结束一个大循环

    while True:
        new_x = x + _x
        new_y = y + _y
        if (new_x, new_y) in result and result[(new_x, new_y)] is None:
            #判断是否有值，是否需要
            i += 1
            result[(new_x, new_y)] = i
            x = new_x
            y = new_y
            flag = 0

        else:
            _x, _y = next(direction)
            flag += 1
            if flag > 4:
                break

    for y in range(h):
        for x in range(w):
            print("%3d"% (result[(x, y)]),end='')
        print()


print_matrix(6, 6, 0, 0)
