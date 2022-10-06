import random
from random import randint              #导入随机函数
print('''
=====================================================================
                             猜拳                                               
=====================================================================
''')

print('''在这个游戏中您将和电脑对战猜拳
         0(石头)
         1(剪刀)                                    
         2(布)
         3或3以上数字(退出游戏)
''')                                                        #游戏介绍
listt = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

jieguo = {0:'石头',
          1:'剪刀',                 #创建字典，每个数字对应一个石头剪刀布
          2:'布',
          }

words = ['象征: ','蜜蜂: ','大象: ','记住: ','重要的: ','公里： ','分钟： ','索道： ','练习:　','遵循；跟着： ','报纸： ','校服： ','桥： ','澳大利亚： ','南非： ']
words_y = {0:'symbol',
           1:'bee',
           2:'elephant',
           3:'remember',
           4:'important',
           5:'kilometer',
           6:'minute',                                              #创建词汇表
           7:'ropeway',
           8:'practice',
           9:'follow',
           10:'newspaper',
           11:'uniform',
           12:'bridge',
           13:'Australia',
           14:'South Africa'}

user_win = 0
computer_win = 0            #设置起始分数和场数
dece = 0
words_true = 0            #设定拼对单词的次数
#======================================================================================================
def pd():
    #判断胜负
    global user_win
    global computer_win
    global dece
    if user_num - computer_num == -1 or user_num - computer_num == 2:
        print('你赢了！'+'\n')
        user_win += 1
        dece += 1
    elif user_num - computer_num == 0:                      #判断谁胜谁负
        print('平局'+'\n')
        
        dece += 1
    else:
        print('电脑胜！'+'\n')
        computer_win += 1
        dece += 1
        cf_hj()                             #调用惩罚函数

def jieguo_gongbu():
    #结果公布                                                        #定义公布结果的函数
    print('=============================================')
    print('本局游戏结束')
    print('您与电脑的比分为:')
    print(str(user_win)+':'+str(computer_win))
    if user_win > computer_win:
        print('你赢了!')
    elif user_win< computer_win:                            #根据玩家和电脑的胜负场数评定赢输
        print('你输了')
    else:
        print('平局了')
    print('=============================================')
    input('请按Enter退出')                          #设置退出选项

def words_true_jilu():
    #计算单词正确率
    if words_true == 4:
        jilu = str((words_true/4)*100)
        print('你居然全拼对了！正确率为'+jilu+'%,你真棒')
    elif words_true == 3:
        jilu = str((words_true/4)*100)
        print('正确率为'+jilu+'%,不错不错!')                    #计算正确率并给予鼓励
    elif words_true == 2 or words_true == 1:
        jilu = str((words_true/4)*100)
        print('正确率为'+jilu+'%,需要努力呀!')
    elif words_true == 0:
        jilu = str((words_true/4)*100)
        print('正确率为'+jilu+'%,居然一个也没拼对！要更加努力背单词了哦！')

def cf_hj():                                                #定义惩罚函数
    #惩罚环节
    global words_true
    print('========================惩罚环节======================')
    print('请输入相对应单词')                                                                    
    print('你答错了还会扣分哦')
    same = random.sample(listt,4)#从listt这个列表中随机抽取5个数字储存在same这个列表中
    words_true = 0            #设定拼对单词的次数   
    for num in same:                           #遍历列表
        nu = num
        x = input(words[nu])
        if x == words_y[nu]:                                                                    
            print('正确')
            words_true += 1    
        else:                                   #判断正确还是错误
            print('错误')
            global user_win
            user_win -= 1
    words_true_jilu()
#========================================================================================================
while dece <= 4:               #若场数小于或等于4就结束循环，公布结果
    try:
        user_num = int(input('请你选择你要出什么:'))
    except ValueError:                                          #告诉python如何处理异常
        print('请输入数字')
        continue
    
    if user_num >= 3:               #若用户输入3或以上数字就退出
        break

    computer_num = randint(0,2)
    print('你出了',jieguo[user_num])                #显示双方出的内容
    print('电脑出了',jieguo[computer_num])
    pd()                                        #调用判定结果的函数

jieguo_gongbu()                                         #调用公布结果的函数
 
