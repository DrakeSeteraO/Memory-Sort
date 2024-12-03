
"""
Purpose:
    This file contains memorySort(), which can sort a list with a time complexity of O(n + m). 
    n = amount of elements in list
    m = distance between the smallest integer and highest integer 
    
    This file also contains variations of the sorting algorithm so that it can be used with different lists

    
Author(s):
    Drake T. Setera

Date:
    12/3/2024

Version:
    3.2.0
"""



def memorySort(lst: list, mode: str = 'i',type = int) -> list:
    """Sorts the inputted list in ascending order utilizing memory to speed up computation time

    Args:
        lst (list): List to get sorted
        
        mode (str): 
        'i' or 'int' = (default) list containing integers
        'n' or 'None' = list containing integers with no repeats
        'c' or 'chr' = list containing characters
        
        type:
        int = (default) list containing integers



    Returns:
        list: sorted list
    """
    if mode == 'i':
        if isinstance(type, int):
            return memorySortI(lst)

    if mode.lower() == 'i' or mode.lower() == 'int':
        return memorySortI(lst)
    if mode.lower() == 'n' or mode.lower() == 'none':
        return memorySortN(lst)
    if mode.lower() == 'c' or mode.lower() == 'chr':
        return memorySortC(lst)
    return None



def memorySortI(lst: list) -> list:
    """Sorts the inputted list of integers in ascending order utilizing memory to speed up computation time

    Args:
        lst (list): List of integers to get sorted

    Returns:
        list: sorted list of integers
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
    p: int = 0
    for o in range(len(amount)):
        for _ in range(amount[o]):
            output[p] = o + low
            p: int = p + 1
          
    return output



def memorySortN(lst: list) -> list:
    """Sorts the inputted list of integers in ascending order utilizing memory to speed up computation time

    Args:
        lst (list): List of integers with no repeating elements as well as
         all elements between the highest and lowest are all used once

    Returns:
        list: sorted list of integers 
    """

    high, low = lst[0], lst[0]
    for l in lst:
        if l > high:
            high: int = l
        elif l < low:
            low: int = l
    ran: int = high - low + 1
    output: list = [None] * ran
    
    for l in lst:
        output[l - low] = l
    return output


def memorySortC(lst: list) -> list:
    """Sorts the inputted list of character elements in ascending order utilizing memory to speed up computation time

    Args:
        lst (list): List of character elements to get sorted

    Returns:
        list: sorted list of character elements
    """
    
    high: int = ord(lst[0])
    low: int = high
    for l in lst:
        temp: int = ord(l)
        if temp > high:
            high: int = temp
        elif temp < low:
            low: int = temp
    ran: int = high - low + 1
    amount: list = [0] * ran
    
    for l in lst:
        amount[ord(l) - low] += 1
    
    output: list = [''] * len(lst)
    p: int = 0
    for o in range(len(amount)):
        for _ in range(amount[o]):
            output[p] = chr(o + low)
            p: int = p + 1
          
    return output
