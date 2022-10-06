
with open('Ten\\wenjian.txt') as la:
    lines = la.readlines()

wenjian_neirong_chucun = ''
for l in lines:
    wenjian_neirong_chucun += l.rstrip()

birthday = input('请输入你的生日，我会测一测你的生日是否在圆周率后1000位;若你的生日为1月7日，那就输入107  ')

if birthday in wenjian_neirong_chucun:
    print('')
    print('你的生日在圆周率后1000位里！')
else:
    print('')
    print('你的生日不在圆周率后1000位里')
print('')
input('请按回车关闭')