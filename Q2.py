def Fitness_Centre():
    choice = input('To get the Senior Citizens discount_30%: press 1: ' 
    	            'If membership is bought and paid for 12 or more months, get 15%_discount: press 2: '
    	            'If more than five personal training sessions are bought and paid for, get 20%_discount on each session: press 3: ')

    if choice == 1:
        Citizens()
        
    elif choice == 2:
        Paid()
    elif choice == 3:
    	Sessions()
    else:
        print "You entered wrong input"


def Citizens():
    cost = float(raw_input('Enter the membership cost: '))
    discounted_membership_cost = cost - (0.3 * cost)
    print "discounted_membership_cost is", discounted_membership_cost

def Paid():
    cost = float(raw_input('Enter the membership cost: '))
    discounted_membership_cost = cost - (0.15 * cost)
    print "discounted_membership_cost is", discounted_membership_cost 

def Sessions():
    cost = float(raw_input('Enter the membership cost: '))
    sessions = int(raw_input('Enter the number of personal training sessions bought: '))
    if sessions <= 5:
    	print "NO discount, membership_cost is", cost
    else:
    	for i in range(0, sessions):
    		discounted_membership_cost = cost - (0.2 * cost)
            print "discounted_membership_cost is", discounted_membership_cost


Fitness_Centre()
