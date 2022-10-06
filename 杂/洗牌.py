def new_func():
    times = 10
    listt = []
    e = 0
    jo = 0
    a = list(range(0,times))
    op = list(range(0,times))
    print('还原过程：')
    while True:
        b = a[:int(times/2)]
        c = a[int(times/2):]
        for bs in b:
            listt.append(bs)
            listt.append(c[jo])
            jo += 1
        a = listt.copy()
        jo = 0
        e += 1
        print(a)
        if listt == op:
            print('还原成功')
            print('洗牌次数:',e)
            break
        listt.clear()       # 重置列表

new_func()