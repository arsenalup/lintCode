# def solution2(s1, s2):
#     alist1 = list(s1)
#     alist2 = list(s2)
#
#     alist1.sort()
#     alist2.sort()
#
#     pos = 0
#     matches = True
#
#     while pos < len(s1) and matches:
#         if alist1[pos] == alist2[pos]:
#             pos +=1
#         else:
#             matches =False
#
#     return matches


def solution3(s1, s2):
    c1 = [0]*26
    c2 = [0]*26
#ord 转数字编码
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    stillok =True
    while j<26 and stillok:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillok = False

    return stillok