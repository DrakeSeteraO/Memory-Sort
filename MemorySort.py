def memorySort(lst: list) -> list:
    """Sorts the inputted list in ascending order utilizing memory to speed up runtime

    Args:
        lst (list): A list containing integers 

    Returns:
        list: A sorted list of integers
    """
    high, low = lst[0], lst[0]
    for l in lst:
        if l > high:
            high: int = l
        elif l < low:
            low: int = l
    ran: int = high - low + 1
    output: list = [None] * ran
    amount = dict()
    
    for l in lst:
        output[l - low] = l
        if l in amount.keys():
            amount[l] = amount[l] + 1
        else:
            amount[l] = 1
    
    output2: list = [0] * len(lst)
    p: int = 0
    for o in output:
        if o is not None:
              for _ in range(amount[o]):
                  output2[p] = o
                  p: int = p + 1     
    return output2
