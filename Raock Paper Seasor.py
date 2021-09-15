import random
#list Of playitem
play_item = ["Rock","Paper","Seasior"]





while True:#To Repeat The code
    computer = play_item[random.randint(0,2)]#Assing playitem to computer
    print(computer)
    print(["Rock","Paper","Seasior?"])
    player = input().capitalize()
    if player == computer:
        print("Opps it's A tie")
    #Rock wins
    elif player == "Rock":
        if computer == "Seasior":
            print("You Win",player,"Smashed",computer)
        else:
            print("You Loos",computer,"Cover",player)

    #paper wins
    elif player == "Paper":
        if computer == "Rock":
            print("You Win",player,"Smashed",computer)
        else:
            print("You Loos",computer,"Cover",player)

    #Seasior wins
    elif player == "Seasior":
        if computer == "Paper":
            print("You Win",player,"Cut's",computer)
        else:
            print("You Loos",computer,"Cover",player)

            #exit
    print("Quit The Game Press 1")
    Exit = int(input())
    if Exit == 1:
        print("Hope You Enjoyed!")
        break
    else:
        pass
            
    
