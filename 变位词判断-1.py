
def solution1(s1, s2):
    alist = list(s2)
    pos1 = 0
    stillok = True

    while pos1 < len(s1) and stillok:
        pos2=0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2+=1

        if found:
            alist[pos2] = None
        else:
            stillok = False

        pos1 +=1
    return stillok

print(solution1('abcd', 'acbd'))
