from functools import reduce


def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


list1 = list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8]))
print(list1)


def expand_list(nested):
    for item in nested:
        if isinstance(item, (list, tuple)):
            for sublist in expand_list(item):
                yield sublist
        else:
            yield item


# reduce(lambda x, y: x + y, nested)
