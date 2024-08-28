"""
演示循环语句的终端控制：break 和 continue
"""
# 循环中断语句 continue
for x in range(1, 6):
    print("语句 1")
    continue
    print("语句 2")

# continue的嵌套应用
for i in range(1, 6):
    print("语句1")
    for j in range(1, 6):
        print("语句 2")
        continue
        print("语句 3")

# 循环中断语句
for x in range(1, 6):
    print("语句 1")
    break
    print("语句 2")

# break的嵌套应用
for r in range (1, 6):
    print("语句 1")
    for h in range (1, 6):
        print("语句 2")
        break
        print("语句 3")