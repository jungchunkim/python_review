from random import *
rn = ["0", "0", "0"]
rn[0] = str(randint(1,9))
rn[1] = str(randint(1,9))
rn[2] = str(randint(1,9))
while rn[0] == rn[1]:
    rn[1] == str(randint(1,9))
while rn[1] == rn[2] or rn[2] == rn[0]:
    rn[2] = str(randint(1,9))

strike = 0
ball = 0
while True:
    g0, g1, g2 = input("Put in three numbers: ").split()
    user = [g0, g1, g2]
    if g0 == rn[0] and g1 == rn[1] and g2 == rn[2]:
        strike += 3
        print("3 Strikes")
    elif g0== rn[0] or g1 == rn[1] or g2 == rn[2]:
        strike += 1
        print("Strike")
    elif g0 == rn[1] or g0 == rn[2] or g1 == rn[0] or g1 == rn[2] or g2 == rn[1] or g2 == rn[0]:
        ball += 1
        print("Ball")
    else:
        ball += 1
        print("Ball")
    print("Computer: {}  User: {}   {}Strike  {}Ball ".format(rn, user, strike, ball ))
    if strike == 3:
        break
    ball = 0
    strike = 0

