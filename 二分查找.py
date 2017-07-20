def search(i, j):
    low, high = 0, len(i)-1
    while low < high:
        print(low, high)
        mid = int((low + high)/2 )
        if i[mid] > j:
            high = mid
        elif i[mid] <j:
            low = mid +1
        else:
            return mid

#     return low if i[low] == j else False

if __name__ == '__main__':
    i = [1, 4, 12, 45, 66, 99, 120, 444]
    print(search(i, 12))
