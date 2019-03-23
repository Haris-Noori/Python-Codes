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
