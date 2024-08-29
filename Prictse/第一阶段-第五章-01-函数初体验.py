"""
演示快速函数的开发及应用
"""

# 需求：统计字符串的长度，不使用内置len()
str1 = "itheima"
str2 = "heart"
str3 = "HYPERION"

# 函数前

count = 0   # 定义初始用来计量长度
for x in str1:
    count += 1
print(count)

count = 0   # 定义初始用来计量长度
for x in str2:
    count += 1
print(count)

count = 0   # 定义初始用来计量长度
for x in str3:
    count += 1
print(count)

# 函数后
def my_len(data):
    count = 0
    for x in data:
        count += 1
    print(count)

my_len(str1)
my_len(str2)
my_len(str3)