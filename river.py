#make lists: left, right
left=["chicken", "fox", "grain"]
right=["0","0","0"]
#make a win boolean
win=False
#make a lose boolean
lose=False
#make a variable to hold which bank the boat is on
boat="left"
boat_swapper=1
temp="empty"
#function to take thing off of one bank
def depart(origin, x):
    for animal in origin:
        if animal==x:
            animal="0"
#function to put things on the new bank
def arrive(destination, y):
    for animal in destination:
        if animal=="0":
            animal=y
            break
#function that checks for lose conditions (either the chicken and grain or chicken and fox are alone in left or right)
def lose_check():
    if (right.count("chicken")==1 and right.count("fox")==1 and right.count("grain")==0) or (left.count("chicken")==1 and left.count("fox")==0 and left.count("grain")==1):
        lose=True
#function that checks for win condition (all three things in right)
def win_check():
    if right.count("0") == 0:
        win=True
#function to print out boat loading
def loading(current):
    print "What do you want to load into the boat?"
    print "1: "+current[0]
    if current[1] != "0":
        print "2: "+current[1]
    else:
        print "2: nothing else"
    if current[2] != "0":
        print "3: "+current[2]
    else:
        print "3: nothing else"
    move_me=input("Please type the corrensponding number.")
    return current[move_me-1]

def bank_check():
    print "Currently, the following are on the left bank:"
    for animal in left:
        if animal != "0":
            print animal

    if right.count("0") != 3:
        print "Currently, the following are on the right bank:"
        for animal in right:
            if animal != "0":
                print animal
    else:
        print "Currently, the right bank is empty"

while win==False and lose==False:
    if boat_swapper % 2 == 0:
        boat="right"
    else:
        boat="left"

    bank_check()
    print "You are on the "+boat+" bank."
    if boat=="left":
        temp=loading(left)
    elif boat=="right":
        temp=loading(right)
    print "You put "+temp+" in the boat."
    print "Set sail?"
    sail=raw_input("Please type yes or no.")
    if boat=="left":
        depart(left, temp)
    elif boat=="right":
        depart(right, temp)

    if sail=="no":
        if boat=="left":
            temp=loading(left)
        elif boat=="right":
            temp=loading(right)
        print "You added "+temp+" to the boat." 
        
        print "Time to cross the river!"
        if boat=="left":
            depart(left, temp)
        elif boat=="right":
            depart(right, temp)

        boat_swapper=boat_swapper+1
        win_check()
        lose_check()

if lose==True:
    print "Sorry, you lose."
    if (right.count("chicken")==1 and right.count("fox")==1 and right.count("grain")==0):
        print "You left the fox and chicken alone. The fox ate the chicken!"
    else:
        print "You left the chicken and grain alone. The chicken ate the grain!"

if win==True:
    print "Congratulations! You got everything across the river!"
    