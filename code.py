

import random as ra

print("Welcome to Rock, Paper, Scissor game\nLet's start")
print('''0 refers to Rock\n1 refers to Paper\n2 refers to Scissor''')

l = int(input("Enter your no(0/1/2):"))
a = [0,1,2]
b = ['Rock','Paper','Scissor']
c = dict(zip(a,b))
r = ra.choice(a)

if(l==0 or l==1 or l==2):

    if (l == r):
        print(f"you chosen {c.get(l)}, computer chosen {c.get(r)}")
        print("It's draw!")

    elif (r > l):

        if (l == 0 and r == 2):
            print(f"you chose {c.get(l)}, computer chose {c.get(r)}")
            print("you won")
        else:
            print(f"you chose {c.get(l)}, computer chose {c.get(r)}")
            print("you lost")

    else:

        if (l == 2 and r == 0):
            print(f"you chose {c.get(l)}, computer chose {c.get(r)}")
            print("you lost")

        else:
            print(f"you chose {c.get(l)}, computer chose {c.get(r)}")
            print("you won")
else:
    print("worng number enterd!")
