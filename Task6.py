def digit_sequence(x):
    for i in x:
        if len(i) == 4:
            if x[i] // 7 == 0:
                return x(i)
        else:
            return None
    
      
digit_sequence([])