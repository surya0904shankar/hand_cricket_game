def user_bowl():
    import random as ran
    out=0
    score=0
    print("     you choose to BOWL")
    rules=""" 
            RULES
            1.you can enter a number from 1 to 6
            2.when you and the system enter the same number the system gets dismissed
            3.till the system becomes out the runs the system score's will be added to its total
            4.once the system becomes out you get the turn of batting
            5.if you score more than the system you win else if you score less than the system, you lose. 
            6.if you both score the same its a draw"""
    print(rules)
    while out!=1:
        user=int(input("enter a number"))
        sys=ran.randint(1,6)
        if user in (1,2,3,4,5,6):
            if sys!=user:
                print("systems output",sys)
                score=score+sys
            elif user==sys:
                print("tthe system is out")
                print("system's total score is",score)
                target=score+1
                out=+1
                return score
                break
        else:
            print("wrong input")

