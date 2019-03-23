# this program counts the number of each vowel alphabet occurs

def question(name):
    a_letters = 0
    e_letters = 0
    i_letters = 0
    o_letters = 0
    u_letters = 0

    for i in name[0:]:
        if i == "a":
            a_letters = a_letters + 1
        if i == "e":
            e_letters = e_letters + 1
        if i == "i":
            i_letters = i_letters + 1
        if i == "o":
            o_letters = o_letters + 1
        if i == "u":
            u_letters = u_letters + 1

    if a_letters > 0:
        print "a comes", a_letters, "times"
    if e_letters > 0:
        print "e comes", e_letters, "times"
    if i_letters > 0:
        print "i comes", i_letters, "times"
    if o_letters > 0:
        print "o comes", o_letters, "times"
    if u_letters > 0:
        print "u comes", u_letters, "times"
    
question()  #input here, inside the brackets



