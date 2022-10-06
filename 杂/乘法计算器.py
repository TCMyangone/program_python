print('==============================乘法计算器===============================')
print('你可以输入 q 退出')

while True:
    f_number = input('请输入第一个数字: ')
    if f_number == 'q':
        break

    l_number = input('请输入第二数字')
    if l_number == 'q':
        break
    
    try:
        jieguo = int(f_number)*int(l_number)
    except ValueError:
        print('无效输入')
    else:
        print(jieguo) 