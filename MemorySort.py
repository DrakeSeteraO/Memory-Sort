def memorySort(lst: list) -> list:
    high, low = lst[0], lst[0]
    for l in lst:
        if l > high:
            high = l
        elif l < low:
            low = l
    ran = high - low + 1
    output = [None] * ran
    amount = dict()
    
    for l in lst:
        output[l - low] = l
        if l in amount.keys():
            amount[l] += 1
        else:
            amount[l] = 1
    
    output2 = list()
    for o in output:
        if o is not None:
              for _ in range(amount[o]):
                  output2.append(o)     
    return output2