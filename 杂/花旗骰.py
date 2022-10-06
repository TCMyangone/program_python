"""
说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3
点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
"""


import random
money = 1000
while money > 0:
    print("您的总资产为:" + str(money))
    n = False
    while True:
        debt = int(input("请下注: "))
        if 0 < debt <= money:
            break
    m = input("请您摇骰子")
    first = random.randint(1, 6) + random.randint(1, 6)
    print("您摇到的点数为:" + str(first))
    if first == 7 or first == 11:
        print("玩家胜!")
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print("庄家胜!")
        money -= debt
    else:
        message = input("您摇到了其他点数,请您继续摇骰子")
        n = True
    while n:
        n =False
        next = random.randint(1, 6) + random.randint(1, 6)
        print("您摇到的点数为:" + str(next))
        if next == 7:
            print("庄家胜!")
            money -= debt   
        elif next == first:
            print("玩家胜!")
            money += debt
        else:
            message = input("您摇到了其他点数,请您继续摇骰子")
            n = True

print("Oh,shit.你破产了!")