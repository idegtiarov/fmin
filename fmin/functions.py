def fmin(array):
    if not array:
        raise ValueError
    array_l = len(array)
    m = array_l // 2
    if m == 0:
        return array[m]
    if array[m - 1] > array[m]:
        return fmin(array[m:]) if array_l > 2 else array[m]
    else:
        return fmin(array[:m]) if m > 1 else array[m - 1]
