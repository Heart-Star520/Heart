"""
演示嵌套应用for循环
"""

# 坚持表白100天，每天都送10朵花
# range 语句

for i in range(1,101):
    print(f"今天是表白的第{i}天")

    # 写内层循环
    for j in range(1, 11):
        print(f"这是今天送的第{j}支花")

    print("我喜欢泥")

print(f"表白的第{i}天，表白成功")