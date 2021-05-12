def magic(square):

    #a square is magic if rows, columns and diagonals all add to the same amount, known as the magic constant
    
    status = None
    
    dim = len(square)
    magic_const =  dim * (dim**2 +1)//2

    #the set function creates a set of the iterable inputted removing any extra duplicates
    #hence can check if each set within the square is equal to the dimension 
    for k in range(dim):
        if dim != len(set(square[k])):
            return 'Invalid data: missing or repeated number'
    
    #if sum of each set/array in square is not magic constant, return not magic square
    for i in square:
        if sum(i) != magic_const:
            return 'Not a magic square'
    
    #if sum of each column is not magic constant, return not magic square 
    for y in range(dim):
        col_sum = 0 
        for row in square:
            col_sum = col_sum + row[y] 
        if col_sum != magic_const:
            return 'Not a magic square'
        
    #if sum of every diagonal is not magic constant, return not magic square
    dia_sum_right = 0
    dia_sum_left = 0
    for y in range(dim):
        dia_sum_right = dia_sum_right + square[y][y]
        dia_sum_left = dia_sum_left + square[dim-1-y][y]
        print((dim-1-y,y))
        
    if dia_sum_right != magic_const or dia_sum_left != magic_const:
        return 'Not a magic square'  
    

    status = 'Magic square'
    
    
    return status