#snake water gun game
import random
actlst=["snake","water","gun"]
print("hello guys let's play snake,water,gun\n ")
winh=0
winc=0
tie=0
i=0
while (i<10):
    print("choose from 1.snake 2.water 3.gun\n")
    print("to choose snake press 's' to choose water press 'w' to choose gun press 'g'\n")
    choiceu = input()
    choice = random.choice(actlst)
    if choiceu=="s":
        if choice=="snake":
            print("computer chose snake\n")
            print("tie\n")
            tie=tie+1
            i=i+1
        elif choice=="water":
            print("computer chose water\n")
            print("You won\n")
            winh=winh+1
            i=i+1
        else :
            print("computer chose gun\n")
            print("You lost\n")
            winc=winc+1
            i = i + 1

    if choiceu=="w":
        if choice=="snake":
            print("computer chose snake\n")
            print("You lost\n")
            winc=winc+1
            i = i + 1
        elif choice=="gun":
            print("computer chose gun\n")
            print("You won\n")
            winh=winh+1
            i = i + 1
        else :
            print("computer chose water\n")
            print("tie\n")
            tie=tie+1
            i = i + 1
    if choiceu=="g":
        if choice=="snake":
            print("computer chose snake\n")
            print("You won\n")
            winh=winh+1
            i = i + 1
        elif choice=="water":
            print("computer chose water\n")
            print("You lost\n")
            winc=winc+1
            i = i + 1
        else :
            print("computer chose gun\n")
            print("tie\n")
            tie=tie+1
            i = i + 1
    else:
        print("Select the correct choice\n")
        continue
print("You won",winh,"times and computer won",winc,"times and there is tie",tie,"times\n")
if winc>winh:
    print("Computer won finally")
elif winh>winc:
    print("You won finally")
else:
    print("There is a tie between you and computer")




