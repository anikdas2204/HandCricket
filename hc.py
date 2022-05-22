import random
runss = [1, 2, 3, 4, 5, 6]              # list used for generating random numbers from1 to 6
toss = {1: "HEAD", 2: "TAIL"}           # dictionary to decide toss result
cd = [1, 2]                             # list to randomly select from for toss purpose

def update_1(a):                        #for updating highest runs
        f = open("hs.txt", 'r')
        data = f.read()
        f.close()
        hs = data.split(",")
        i = int(hs[0])
        if a > i:
            b = hs[1]
            f = open("hs.txt", 'w')
            f.close()
            f = open("hs.txt", 'a')
            f.write(str(a))
            f.write(",")
            f.write(str(b))
            f.close()
    
def update_2(a):                         #for updating best bowling
    f = open("hs.txt", 'r')
    data = f.read()
    f.close()
    hs = data.split(",")
    i = int(hs[1])
    if a < i:
        b = hs[0]
        f = open("hs.txt", 'w')
        f.close()
        f = open("hs.txt", 'a')
        f.write(str(b))
        f.write(",")
        f.write(str(a))
        f.close()

def batfirst(pl):                           #First inning -- setting target by the batsman
    o = 0
    score = 0

    if pl == 'c':                           #User bowling to computer
        print("\n")
        print("FIRST INNINGS")
        print("X--X--X--X--X--X--X--X--X--X")
        while o == 0:
            e = 0
            while e == 0:
                b = int(input("Enter Your Bowling choice 1-6: "))
                if b > 6 or b < 1:
                    print("SELECT BETWEEN 1-6")
                    e = 0
                else:
                    r = random.choice(runss)
                    e = 1
                if b == r:
                    o = 1
                    e = 1
                    print("COMPUTER HIT: ", r)
                    print("COMPUTER IS OUT!!!")
                    print("SCORE: ", score)
                    break
                else:
                    print("COMPUTER SCORED: ", r)
                    score = score+r
                    print("SCORE: ", score)
        update_2(score)
        return score
    else:                                   #User batting
        print("\n")
        print("FIRST INNINGS")
        print("X--X--X--X--X--X--X--X--X--X")
        while o == 0:
            e = 0
            while e == 0:
                r = int(input("Enter Your Batting choice 1-6: "))
                if r > 6 or r < 1:
                    print("SELECT BETWEEN 1-6")
                    e = 0
                else:
                    e = 1
                    b = random.choice(runss)
                if b == r:
                    o = 1
                    e = 1
                    print("COMPUTER BOWLED: ", b)
                    print("YOU ARE OUT!!!")
                    print("SCORE: ", score)
                    break
                else:
                    print("YOU SCORED: ", r)
                    score = score+r
                    print("SCORE: ", score)
        update_1(score)
        return score


def batsec(pl, sc):                 #Second inning -- target already given
    o = 0
    score = 0
    if pl == 'c':                   
        print("SECOND INNINGS")
        print("X--X--X--X--X--X--X--X--X--X")
        while o == 0 and score <= sc:
            e = 0
            r = random.choice(runss)
            while e == 0:
                b = int(input("Enter Your Bowling choice 1-6: "))
                if b > 6 or b < 1:
                    print("SELECT BETWEEN 1-6")
                    e = 0
                else:
                    e = 1
                if b == r:
                    o = 1
                    e = 1
                    print("COMPUTER HIT: ", r)
                    print("COMPUTER IS OUT!!!")
                    print("SCORE: ", score)
                    if score < sc:
                        print("YOU WON BY: ", sc-score, " RUNS!!!")
                    elif score == sc:
                        print("MATCH DRAWN!!!")
                    else:
                        continue
                else:
                    score = score+r
                    print("Score: ", score)
                    if (sc-score+1) > 0:
                        print("RUNS NEEDED: ", (sc-score)+1)
                    else:
                        print("RUNS NEEDED: ", 0)
                    if score > sc:
                        print("COMPUTER WIN!!!")
        update_2(score)                
    else:
        print("SECOND INNINGS")
        print("X--X--X--X--X--X--X--X--X--X")
        while o == 0 and score <= sc:
            e = 0
            while e == 0:
                r = int(input("Enter Your Batting Choice 1-6: "))
                if r > 6 or r < 1:
                    print("SELECT BETWEEN 1-6")
                    e = 0
                else:
                    e = 1
                    b = random.randint(1, 6)
            if b == r:
                o = 1
                e = 1
                print("COMPUTER BOWLED: ", b)
                print("YOU ARE OUT!!!")
                print("SCORE: ", score)
                if score < sc:
                    print("YOU LOSS BY: ", sc-score, " RUNS")
                elif score == sc:
                    print("MATCH DRAWN!!!")
            else:
                score = score+r
                print("Score: ", score)
                if (sc-score+1) > 0:
                    print("RUNS NEEDED: ", (sc-score)+1)
                else:
                    print("RUNS NEEDED: ", 0)
                if score > sc:
                    print("YOU WIN!!!")
        update_1(score)            


pl = int(input("1.PLAY\n2.RULES\n3.HIGH SCORE\n4.DESCRIPTION\n5.EXIT\nENTER YOUR CHOICE: "))
while pl != 5:
    if pl == 1:
        print("YOU CAN SELECT ANY NUMBER BETWEEN 1-6 !!! YOU HAVE ONE WICKET IN YOUR HAND")
        print("!!! *** COIN IS TOSSED *** !!!!")
        ch = int(input("1.HEAD\n2.TAIL\nWHATS YOUR CALL? : "))
        j = random.choice(cd)
        if j == 1:
            t = "HEAD"
        else:
            t = "TAIL"
        if(toss[ch] == t):
            print(toss[ch], " WAS THE CALL\n AND ITS ", t)
            print("YOU WON THE TOSS!!!")
            u = 1
        else:
            print(toss[ch], " WAS THE CALL\n AND ITS ", t)
            print("YOU LOSS THE TOSS!!!")
            u = 0
        if u == 1:
            d = int(input("1.BAT\n2.BOWL\nWHAT YOU WANT TO DO FIRST: "))
            if d == 1:
                sc = batfirst('u')
                print("\n")
                batsec('c', sc)
            else:
                sc = batfirst('c')
                print("\n")
                batsec('u', sc)
        else:
            d = random.choice(cd)
            if d == 1:
                print("COMPUTER WILL BAT FIRST !!!")
                sc = batfirst('c')
                print("\n")
                batsec('u', sc)
            else:
                print("COMPUTER WILL BOWL FIRST !!!")
                sc = batfirst('u')
                print("\n")
                batsec('c', sc)
    elif pl == 2:
        f = open("rules.txt", 'r')
        data = f.read()
        print(data)
        f.close()
    elif pl == 3:
        f = open("hs.txt", 'r')
        data = f.read()
        hs = data.split(",")
        print("\nHIGHEST SCORE TILL NOW IS")
        print("RUNS SCORED IN ONE MATCH: ",
              hs[0], "RUNS     LOWEST RUN GIVEN TO COMPUTER: ", hs[1], "RUNS\n")
        f.close()
    elif pl == 4:
        f = open("desc.txt", 'r')
        data = f.read()
        print(data)
        f.close()

    pl = int(input("1.PLAY\n2.RULES\n3.HIGH SCORE\n4.DESCRIPTION\n5.EXIT\nENTER YOUR CHOICE: "))

