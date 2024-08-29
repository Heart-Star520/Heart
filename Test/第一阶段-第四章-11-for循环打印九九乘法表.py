"""
for 嵌套打印九九乘法表
"""

for x in range(1, 10):
    print("")
    for y in range(1, x + 1):
        print(f"{x}x{y}={x*y}", end="\t")