"""
规则：
完全按照 斗地主 的积分方式
"""

print("欢迎使用由 Heart-Star520 自主研发的： 斗地主 积分器\n制作者GITHUB主页：https://github.com/Heart-Star520")

# 定义有几位玩家，变量 user_count
user_count = int(input("本次游玩有几位玩家？\n"))

# 定义玩家命列表
player_name = []
player_count = []

# 让用户给每位玩家取名
tem_count = 1 # 临时计算每次玩家在while循环的数量
while tem_count <= user_count:
    tem_use_user_name = str(input(f"请给第 {tem_count} 位玩家取名\n"))
    player_name.append(tem_use_user_name)   # 讲玩家输入的用户名加入列表
    player_count.append(tem_use_user_name)
    tem_count += 1  # 及时在到达上限后退出循环

# 为用户输出本次所有用户名
print(f"[———— 用户名输入完毕 ————]\n总共有 {user_count} 位玩家，玩家名分别是")

# 临时变量用于计算要输出多少次print
tem_get_user = 1    # 用于给玩家显示
tem_get_name_2 = 0  # 用于输出列表名称
while tem_get_user <= user_count:
    print(f"编号 {tem_get_user} ：{player_name[tem_get_name_2]}")
    player_count[tem_get_name_2] = 0 # 顺带定义每个列表元素（玩家）的分数
    tem_get_user += 1
    tem_get_name_2 += 1

connent = 0  # 初始化循环控制变量

while connent < 1:  # 你可以调整这个条件来控制循环次数
    print("[———— 进入计分阶段 ————]")
    place_owner = int(input("哪位玩家是地主（输入玩家编号1,2,3,4...）：\n"))  # 定义地主
    print("地主：", player_name[place_owner - 1])

    every_end = str(input(f"[———— 游戏结束 ————]\n本次比赛地主 {player_name[place_owner - 1]} 赢了吗（输入y/n）？\n"))

    if every_end == "y":
        every_get_count = int(input("地主赢了多少分（只需要输入地主 要的分 * 本局的翻倍数的结果）：\n"))
        tem_player_count = user_count - 1
        player_count[place_owner - 1] += every_get_count * tem_player_count + every_get_count  # 增加地主分数,1.5是为了抵消下面全员减分
        for i in range(len(player_count)):  # 将所有人的分数 - 地主要的分
            player_count[i] -= every_get_count

    elif every_end == "n":
        every_get_count = int(input("地主输了多少分（只需要输入地主 要的分 * 本局的翻倍数的结果）：\n"))
        tem_player_count = user_count - 1
        player_count[place_owner - 1] -= every_get_count * tem_player_count - every_get_count  # 减少地主分数,1.5是为了抵消下面全员加分
        for i in range(len(player_count)):  # 将所有人的分数 + 地主要的分
            player_count[i] += every_get_count

    # 打印当前所有玩家的分数
    print(f"[———— 分数统计 ————]\n总共有 {user_count} 位玩家，现在玩家分别有积分：\n")

    tem_get_user = 1  # 用于给玩家显示
    tem_get_name_2 = 0  # 用于输出列表名称
    while tem_get_user <= user_count:
        print(f"{player_name[tem_get_name_2]} ：{player_count[tem_get_name_2]}")
        tem_get_user += 1
        tem_get_name_2 += 1

    # 你可以根据需要增加更多逻辑，比如是否继续进行下一轮游戏
    continue_game = input("[———— 是否继续下一轮游戏(y/n) ————]\n")
    if continue_game.lower() == "n":
        break  # 退出循环
