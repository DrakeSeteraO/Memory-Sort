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
    amount: list = [0] * ran
    
    for l in lst:
        amount[l - low] += 1
    
    output: list = [0] * len(lst)
    p = 0
    for o in range(len(amount)):
        for _ in range(amount[o]):
            output[p] = o + low
            p: int = p + 1
          
    return output
