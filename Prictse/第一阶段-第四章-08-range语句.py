"""
演示Python中的range()语句的基础使用
"""

#range 语法1 range(num)
for x in range(10):
    print(x)

# range 语法2 range(num1, num2)
for x in range(5, 10):
    print(x)

# range 语法3 range(num1, num2, step)
# step: 默认是 1 ，表示每此x获取的数步长 1，如果不懂，可以修改下面数字'5'位其它数字
for x in range(10, 100, 5):
    print(x)