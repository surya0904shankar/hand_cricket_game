
import system_bat
import system_bowl
import user_bat
import user_bowl

import random as ran
while True:
    print("welcome to the hand cricket carnival")
    op=int(input("Enter 1 to choose ODD , Enter 2 to choose EVEN for playing the toss"))
    if op==1:
        toss1=int(input("enter a number between 1 TO 6 for playing the toss"))
        toss2=ran.randint(1,6)
        while True:
            if toss1 in (1,2,3,4,5,6):
                final=toss1+toss2
                if final%2!=0:
                    print("you won the toss")
                    play=input('enter BAT to choose batting and enter BOWL to choose bowling')
                    final=1##

                    if play=="BAT":
                        sc1=user_bat.user_bat() 
                        print("your score",sc1)
                        print("systems target",sc1+1)
                        print()
                        sc2= system_bat.system_bat()
                        print("systems score",sc2)
                        print()
                       
                        if sc1==sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE=",sc2)
                           print("IT IS A DRAW")
                        elif sc1>sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("YOU WIN THE MATCH BY",sc1-sc2, "RUNS")
                        elif sc2>sc1:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("SYSTEM WIN'S THE MATCH BY",sc2-sc1, "RUNS")
                           break

                    elif play=="BOWL":
                        sc2=user_bowl.user_bowl()
                        print("systems score",sc2)
                        print("your target",sc2+1)
                        print()
                        sc1= system_bowl.system_bowl()
                        print("your score",sc1)
                        print()
                        if sc1==sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE=",sc2)
                           print("IT IS A DRAW")
                        elif sc1>sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("YOU WIN THE MATCH BY",sc1-sc2, "RUNS")
                        elif sc2>sc1:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("SYSTEM WIN'S THE MATCH BY",sc2-sc1, "RUNS")
                           break
                       

                else:
                    print("system won the toss")

                    play=ran.choice(['BAT','BOWL'])
                    if play=="BAT":
                        sc2=system_bat.system_bat()
                        print("systems score",sc2)
                        print("your target",sc2+1)
                        print()
                        sc1=user_bat.user_bat()
                        print("your score",sc1)
                        print()
                        if sc1==sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE=",sc2)
                           print("IT IS A DRAW")
                        elif sc1>sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("YOU WIN THE MATCH BY",sc1-sc2, "RUNS")
                        elif sc2>sc1:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("SYSTEM WIN'S THE MATCH BY",sc2-sc1, "RUNS")
                       
                        break
                    elif play=="BOWL":
                        sc1=system_bowl.system_bowl()
                        print("your score",sc1)
                        print("systems target",sc1+1)
                        print()
                        sc2=user_bowl.user_bowl()
                        print("systms score",sc2)
                        print()
                        if sc1==sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE=",sc2)
                           print("IT IS A DRAW")
                        elif sc1>sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE=",sc2)
                           print("YOU WIN THE MATCH BY",sc1-sc2, "RUNS")
                        elif sc2>sc1:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE=",sc2)
                           print("SYSTEM WIN'S THE MATCH BY",sc2-sc1, "RUNS")
                       
                        break
            else:
                print("wrong input")
                break
            
    elif op==2:
        toss1=int(input("enter a number between 1 TO 6 for playing the toss"))
        toss2=ran.randint(1,6)
        while True:
            if toss1 in (1,2,3,4,5,6):
                final=toss1+toss2
                if final%2==0:
                    print("you won the toss")
                    play=input('enter BAT to choose batting and enter BOWL to choose bowling')
                    if play=="BAT":

                       sc1=user_bat.user_bat() 
                       print("your score",sc1)
                       print("systems target",sc1+1)
                       print()
                       
                       sc2= system_bat.system_bat()
                       print("systems score",sc2)
                       print()
                       
                       if sc1==sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE=",sc2)
                           print("IT IS A DRAW")
                       elif sc1>sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("YOU WIN THE MATCH BY",sc1-sc2, "RUNS")
                       elif sc2>sc1:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("SYSTEM WIN'S THE MATCH BY",sc2-sc1, "RUNS")

                       break
                    elif play=="BOWL":
                        sc2=user_bowl.user_bowl()
                        print("systems score",sc2)
                        print("your target",sc2+1)
                        print()
                        sc1= system_bowl.system_bowl()
                        print("your score",sc1)
                        print()
                        if sc1==sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE=",sc2)
                           print("IT IS A DRAW")
                        elif sc1>sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("YOU WIN THE MATCH BY",sc1-sc2, "RUNS")
                        elif sc2>sc1:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("SYSTEM WIN'S THE MATCH BY",sc2-sc1, "RUNS")
                       

                        break
                else:
                    print("system won the toss")

                    play=ran.choice(['BAT','BOWL'])
                    if play=="BAT":
                        sc2=system_bat.system_bat()
                        print("systems score",sc2)
                        print("your target",sc2+1)
                        print()
                        sc1=user_bat.user_bat()
                        print("your score",sc1)
                        print()
                        if sc1==sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE=",sc2)
                           print("IT IS A DRAW")
                        elif sc1>sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("YOU WIN THE MATCH BY",sc1-sc2, "RUNS")
                        elif sc2>sc1:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("SYSTEM WIN'S THE MATCH BY",sc2-sc1, "RUNS")
                       
                        break
                    elif play=="BOWL":
                        sc1=system_bowl.system_bowl()
                        print("your score",sc1)
                        print("systems target",sc1+1)
                        print()
                        sc2=user_bowl.user_bowl()
                        print("systms score",sc1)
                        print()
                        if sc1==sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE=",sc2)
                           print("IT IS A DRAW")
                        elif sc1>sc2:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("YOU WIN THE MATCH BY",sc1-sc2, "RUNS")
                        elif sc2>sc1:
                           print("YOUR SCORE=",sc1,"SYSTEM'S SCORE",sc2)
                           print("SYSTEM WIN'S THE MATCH BY",sc2-sc1, "RUNS")
                       
                        break
            else:
                print("wrong input")
                break
    else: 
        print('wrong input try again')
