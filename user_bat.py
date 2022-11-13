def user_bat():
    import random as ran
    out=0
    score=0
    target=0
    print("        you choose to BAT")
    rules="""
            RULES
            1.you can enter a number from 1 to 6
            2.when you and the system enter the same number you are dismissed
            3.till you become out the runs you score will be added to your total
            4.once you become out the system plays the turn of batting
            5.if the system scores more than you it wins else if it scores less than you, you win. 
            6.if you both score the same its a draw"""
    print(rules)
    while out!=1:
        user=int(input("enter a number"))
        sys=ran.randint(1,6)
        if user in (1,2,3,4,5,6):
            if user!=sys:
                print("systems output",sys)
                score=score+user
            elif user==sys:
                print("systems output",sys)
                print("you are out")
                print("your total score is",score)
                target=score+1
                out=out+1
                return score
                break
        else:
            print("wrong input")
    return target
        

