
"""
Purpose:
    This file contains memorySort(), which can sort a list with a time complexity of O(n + m). 
    n = amount of elements in list
    m = distance between the smallest integer and highest integer 
    
    This file also contains variations of the sorting algorithm so that it can be used with different lists

    
Author(s):
    Drake T. Setera

Date:
    11/25/2024

Version:
    3.1.0
"""



def memorySort(lst: list, mode: str = 'i') -> list:
    """Sorts the inputted list in ascending order utilizing memory to speed up computation time

    Args:
        lst (list): List to get sorted
        mode (str): 
        'i' = (default) list containing integers
        'n' = list containing integers with no repeats
        'c' = list containing characters

    Returns:
        list: sorted list
    """
    
    if mode.lower() == 'i':
        return memorySortI(lst)
    if mode.lower() == 'n':
        return memorySortN(lst)
    if mode.lower() == 'c':
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
            high = l
        elif l < low:
            low = l
    ran = high - low + 1
    output = [None] * ran
    
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
    
    high, low = ord(lst[0]), ord(lst[0])
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
    
    output: list = [0] * len(lst)
    p: int = 0
    for o in range(len(amount)):
        for _ in range(amount[o]):
            output[p] = chr(o + low)
            p: int = p + 1
          
    return output