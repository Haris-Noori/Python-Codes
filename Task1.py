for number in range(1500, 2700):
    if type(number // 7) == int and number & 5 == 0:
        print number




def Temperature():
    choice = input('To convert into Farehite:press 1: '
                       'To convert into Celsius:press 2: ')

    if choice == 1:
        Farenhite()
        
    elif choice == 2:
        Celsius()
    else:
        print "You entered wrong input"
        
def Farenhite():
    F = float(raw_input('Enter Temperature in Celsius: '))
    Degree = (F * 1.8) + 32
    return "Temperature in Farenhite", Degree

def Celsius():
    C = float(raw_input('Enter Temperature in Farenhite: '))
    Degree = (C - 32) / 1.8
    return "Temperature in Celsius", Degree

Temperature()






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





for h in range (1,10):
    if h == 1:
        print "*"
    if h == 2:
        print "*","*"
    if h == 3:
        print "*", "*", "*"
    if h == 4:
        print "*", "*", "*", "*"
    if h == 5:
        print "*", "*", "*", "*", "*"
    if h == 6:
        print "*","*", "*", "*"
    if h == 7:
        print "*", "*", "*"
    if h == 8:
        print "*", "*"
    if h == 9:
        print "*"






for number in range(1, 51):
    if number % 3 == 0:
        print "Fizz"
    if number % 5 == 0:
        print "Buzz"
    if number % 5 == 0 and number % 3 == 0:
        print "FizzBuzz"








def digit_sequence(x):
    for i in x:
        if len(i) == 4:
            if x[i] // 7 == 0:
                return x(i)
        else:
            return None
    
      
digit_sequence([])