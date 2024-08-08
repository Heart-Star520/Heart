# 数一数有几个a

name = "itheima is a brand of itcast" # 定义变量
chance = 0 # 定义有几个a的变量

for x in name:
    # 写一个if语法，如果x是a，chance就增加1
    if x == "a":
        chance += 1

# 结束后打印结果
print(f"itheima is a brand of itcast中共有：{chance}个字母a")