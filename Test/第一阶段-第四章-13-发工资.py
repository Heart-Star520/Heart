"""
发工资
"""
import random
com_balance = 10000
for x in range(1, 21):  # 循环20位员工
    tem_number = random.randint(1, 10)
    if com_balance != 0:
        if tem_number < 5:
            print(f"员工{x}，绩效分{tem_number}，低于5，不发工资，下一位")
            continue
        else:
            com_balance -= 1000
            print(f"向员工{x}发放1000元，账户余额还剩余{com_balance}")
    else:
        print("工资发完了，下个月再来吧")
        break
