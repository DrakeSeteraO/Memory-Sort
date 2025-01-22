
"""
Purpose:
    This file contains memorySort(), which can sort a list with a time complexity of O(n + k). 
    n = amount of elements in list
    k = distance between the smallest integer and highest integer 
    
    This file also contains variations of the sorting algorithm so that it can be used with lists containing different object types

    
Author(s):
    Drake T. Setera

Date:
    1/21/2025

Version:
    5.1.0
"""



def memorySort(lst: list, mode: str = '') -> list:
    """Sorts the inputted list in ascending order utilizing memory to speed up computation time

    Args:
        lst (list): List to get sorted
        
        mode (str):
        : (default) = sorts list using mode of first element in the given list 
        : 'a' or 'ascii' = list containing strings (sorted based on string ascii value)
        : 'c' or 'chr' = list containing characters
        : 'f' or 'float' = list containing float
        : 'i' or 'int' = list containing integers
        : 'n' or 'None' = list containing integers with no repeats
        : 's' or 'str' = list containing strings (sorted based on letter order)



    Returns:
        list: sorted list
    """


    if mode == '':
        if isinstance(lst, list):
            if isinstance(lst[0], int):
                return memorySortI(lst)
            if isinstance(lst[0], float):
                return memorySortF(lst)
            if isinstance(lst[0], str):
                return memorySortS(lst)
        elif isinstance(lst, str):
                return memorySortString(lst)


    if mode.lower() == 'i' or mode.lower() == 'int' or mode.lower() == '':
        return memorySortI(lst)
    if mode.lower() == 'f' or mode.lower() == 'float':
        return memorySortF(lst)
    if mode.lower() == 'n' or mode.lower() == 'none':
        return memorySortN(lst)
    if mode.lower() == 'c' or mode.lower() == 'chr':
        return memorySortC(lst)
    if mode.lower() == 's' or mode.lower() == 'str':
        return memorySortS(lst)
    if mode.lower() == 'a' or mode.lower() == 'ascii':
        return memorySortA(lst)
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



def memorySortA(lst: list) -> list:
    """Sorts the inputted list of string elements in ascending order based on ascii value utilizing memory to speed up computation time

    Args:
        lst (list): List of string elements to get sorted

    Returns:
        list: sorted list of string elements
    """

    
    high: int = 0
    for l in lst[0]:
        high = high * 128 + ord(l)
    low: int = high

    
    for l in lst:
        temp: int = 0
        for i in l:
           temp = temp * 128 + ord(i)
         
        if temp > high:
            high: int = temp
        elif temp < low:
            low: int = temp
    
    
    ran: int = high - low + 1
    amount: list = [0] * ran
    
    for l in lst:
        temp: int = 0
        for i in l:
           temp = temp * 128 + ord(i)
        amount[temp - low] += 1

    
    output: list = [''] * len(lst)
    p: int = 0
    for o in range(len(amount)):
        if amount[o] != 0:
            i = o + low
            out = ''
            while i != 0:
                letter = chr(i % 128)
                i = i // 128
                out = letter + out
        
            for _ in range(amount[o]):
                output[p] = out
                p: int = p + 1

          
    return output



def memorySortF(lst: list) -> list:
    """Sorts the inputted list of float in ascending order utilizing memory to speed up computation time

    Args:
        lst (list): List of float to get sorted

    Returns:
        list: sorted list of float
    """
 
    
    high, low = int(lst[0]), int(lst[0])
    for l in lst:
        temp = int(l)
        if temp > high:
            high: int = temp
        elif temp < low:
            low: int = temp
    ran: int = high - low + 1
    amount: list = [0] * ran
 
    
    for l in lst:
        if amount[int(l) - low] == 0:
           amount[int(l) - low] = [l] 
        else:
           amount[int(l) - low].append(l)
 
    
    output: list = [0] * len(lst)
    p: int = 0       
    for am in amount:
        if isinstance(am,list):
            am.sort() 
            for a in am:
                output[p] = a
                p: int = p + 1
 
          
    return output



def memorySortS(lst: list) -> list:
    """Sorts the inputted list of string elements in ascending order utilizing memory to speed up computation time

    Args:
        lst (list): List of string elements to get sorted

    Returns:
        list: sorted list of string elements
    """
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst
    
    
    high: int = -1
    low: int = 256
    for l in lst:
        if len(l) > 0:
            temp: int = ord(l[0])
            if temp > high:
                high: int = temp
            if temp < low:
                low: int = temp
   
            
    if (low == high) or (low == 256 and high == -1):
        return lst        

            
    ran: int = high - low + 1
    amount: list = [0] * ran
 
    
    for l in lst:
        if amount[ord(l[0]) - low] == 0:
           amount[ord(l[0]) - low] = [l] 
        else:
           amount[ord(l[0]) - low].append(l)
  
  
    for am in range(len(amount)):
        if isinstance(amount[am], list):
            for a in range(len(amount[am])):
                amount[am][a] = amount[am][a][1:]
            
            amount[am] = memorySortS(amount[am])
        
  
    output: list = [''] * len(lst)
    p: int = 0
    for o in range(len(amount)):
        if isinstance(amount[o], list):
            for a in range(len(amount[o])):
                output[p] = chr(o + low) + amount[o][a]
                p: int = p + 1
          
    return output



def memorySortString(string: str) -> str:
    temp = memorySortC(string)
    output = ''
        
    for t in temp:
        output = output + t
    
    return output