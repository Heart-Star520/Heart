# 设置变量记录有几个偶数
count = 0

# 使用 for 结合 range 语句
for x in range(1, 100):
    # 使用if语句判断是否为偶数
    if x % 2 == 0: # %: 除余
        count += 1

print(f"1到100（不含100本身）范围内，有{count}个偶数")
