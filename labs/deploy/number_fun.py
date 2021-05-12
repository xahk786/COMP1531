import typing

def multiply_by_two(number : (int, float)):
    '''
    Multiplies a given number by two.
    '''
    num = int(number) * 2
    return num

def print_message(message : (str) ):
    '''
    Prints a given message.
    '''
    return message

def sum_list_of_numbers(numbers : (list, int, float)):
    '''
    Returns the sum of a list of numbers
    '''
    summ = 0
     
    lst = numbers
    lst = [ int(x) for x in lst ]
    
    for i in lst:
        summ = summ + i
    
    return summ
    

def sum_iterable_of_numbers(numbers : (list, tuple, dict, int, float)):
    '''
    Calculates the sum of an iterable of numbers

    numbers: any iterable

    Return value: integer
    '''
    
    lst = numbers
    lst = [ int(x) for x in lst ]
    
    
    if len(lst) == 1:
        final = (lst[0])
       
    else:
        summ = sum(lst)
        final = (summ)
        
    return final

def is_in(needle : (str, int) , haystack: (list, str, int)):
    '''
    Checks if the given item is in a list

    Parameters:
    - needle: a string or an integer
    - haystack: a list of strings or integers

    Return value: bool - if the needle is in the haystack
    '''
    if needle in haystack:
        check = True
    else:
        check = False
    
    return check
    

def index_of_number(item : (int) , numbers : (list, int)):
    '''
    Returns the index of the given item in a list of numbers

    Parameters:
    - item: an integer
    - numbers: a list of numbers

    Return value: the index of the item, or None if the items is not in numbers
    '''
    numbers = [ int(x) for x in numbers ]
    item = int(item)
    
    i = 0
    
    for x in numbers:        
        if x == item:   
        #found!!!
            return i
        i = i + 1
        
    not_found = True
    if not_found:
        return None