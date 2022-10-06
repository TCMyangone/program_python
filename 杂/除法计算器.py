print('=======================================除法计算器==========================================')
print('若你想退出，请输入q')

while True:
    f_number = input('第一个数字: ')
    if f_number == 'q':
        break

    l_number = input('第二个数字: ')
    if l_number == 'q':
        break
    try:
        angser = int(f_number)/int(l_number)
    except ZeroDivisionError:
        print('你不能除以0')
    except ValueError:
        print('无效输入')
    else:
        print(angser)