"""
斐波那契数列
"""
line = 4
space = 0
row = int(input("生成的行数: "))
# for i in range(row):
#     if 0 < space < line:
#         for j in range(space):
#             print(" ", end = "")
#     elif space >= line:
#         space -= 1
            
#     print("x")
#     space += 1
way = 1
for i in range(row):
    for j in range(space):
        print(" ", end = "")
    print("x")
    space += way
    if space == line - 1:
        way *= -1
    elif space == 0:
        way *= -1

