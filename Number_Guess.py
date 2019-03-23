def number_guess():
    print "Enter any number from range 1---9"
    a = 5
    choice = int(raw_input('Enter a guess: '))
    
    if choice == a:
        print "Well guessed!"
    
    elif choice != a:
        number_guess()
        
    else:
        print "Please enter a number only from 1---9"
        
number_guess()
