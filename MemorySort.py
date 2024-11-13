def memorySort(lst: list) -> list:
    high, low = lst[0], lst[0]
    for l in lst:
        if l > high:
            high = l
        elif l < low:
            low = l
    ran = high - low + 1
    output = [None] * ran
    
    for l in lst:
        output[l - low] = l
    return output