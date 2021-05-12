def roman(numerals):
    '''
    Given Roman numerals as a string, return their value as an integer. You may
    assume the Roman numerals are in the "standard" form, i.e. any digits
    involving 4 and 9 will always appear in the subtractive form.
    '''
    tup_list = [
               ('I', 1),
               ('V', 5),
               ('X', 10),
               ("L", 50),
               ('C', 100),
               ('D', 500),
               ('M', 1000)
               ]
               
    char_num_next = 0
    num = 0
    i=0
    
    while i < len(numerals):
        if i != (len(numerals) - 1):
            for y_next in tup_list:
                if y_next[0] == numerals[i+1]:
                    char_num_next = y_next[1]

        for y in tup_list:
            if y[0] == numerals[i]:
                char_num = y[1]
        
        if char_num >= char_num_next:
            num = num + char_num
        
        elif char_num < char_num_next:
            before = char_num_next - char_num
            num = num + before
            i = i +1 

        i+=1     
         
    return num   

    
