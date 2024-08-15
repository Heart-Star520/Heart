# 随机物品价格
import random

# 统计总共花费额
money = 0

# 我买的东西价格

cost = 0    # 定义商品价格
count = 0   # 总共商品件数
cost_list = []
tem_cost = 0
# 买99天东西的价格

for day in range(1, 100):
    # 第一天买
    if day == 1:
        print(f"————————[第一天买东西]——————————")
        # 定义x，买的次数，每次买99个
        x = 1
        while x < 99:
            # 要价随机加
            tem_cost = random.randint(1, 10)
            cost_list.append(tem_cost)  # 将本次要价加入统计列表
            cost += tem_cost
            print(f"本次要价{cost}")
            x += 1
            money += cost
            print(f"第{x}件东西，价格{cost}元，总共花了{money}")
    # 多次买
    else:
        print(f"————————[第{x}天买东西]——————————")
        # 定义x，买的次数，每次买99个
        x = 1
        while x < 99:
            # 加商品件数1
            count += 1
            # 要价随机加

            tem_cost = random.randint(1, 1000)
            cost_list.append(tem_cost)  # 将本次要价加入统计列表
            cost += tem_cost
            print(f"本次要价{cost}")
            x += 1
            money += cost
            print(f"第{x}件东西，价格{cost}元，总共花了{money}")

print(f"———— {day} 天结束 ————\n总共花费{money}元\n总共购买件数：{count}\n每次要价：{cost_list}\n")
