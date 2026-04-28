# 字符串，列表，元组，字典，集合都是数据容器
# sorted 函数，返回一个排序后的新容器（不改变原容器，默认顺序：从小到大）
# 都是数字，则按照数字的大小顺序进行排序。
# key 函数：这是它的“灵魂”。你可以告诉 Python 按什么标准排。
# 按绝对值排：sorted([-5, 2, -1], key=abs)
# 按长度排：sorted(["apple", "ok", "banana"], key=len)
nums = [23, 11, 32, 30, 17]
result = sorted(nums, reverse=True)
print(nums)   # [23, 11, 32, 30, 17]
print(result) # [32, 30, 23, 17, 11]

# 既有数字，又有字符串，那就会报错。
nums = [23, 11, 32, 30, 17, '尚硅谷']
# sorted(nums)

# 都是字符串，则按照字符串的 Unicode 编码大小进行排序。
msg_list = ['北京', '尚硅谷', '你好']
result = sorted(msg_list)
print(msg_list)  # ['北京', '尚硅谷', '你好']
print(result) # ['你好', '北京', '尚硅谷']

# len 函数，获取容器中元素的总数量，返回值是：元素总数量。
nums = [10, 20, 10, 30, 10, 40, [50, 60, 70]]
result = len(nums)
print(result) # 7

# max 函数，获取容器中的最大值，返回值是：最大值。
# 都是数字，那 max 返回的是最大的数。
nums = [23, 11, 32, 30, 17]
result = max(nums)
print(nums) # [23, 11, 32, 30, 17]
print(result) # 32

# 既有数字又有字符串，那 max 会报错。
nums = [23, 11, 32, 30, 17, '尚硅谷']
# max(nums)

# 都是字符串，那 max 会返回：Unicode 编码最大的字符。
msg_list = ['北京', '尚硅谷', '你好']
result = max(msg_list)
print(msg_list)  # ['北京', '尚硅谷', '你好']
print(result)  # 尚硅谷
print(ord('北'))  # 21271
print(chr(21271))  # 北

# max 函数也可以接收多个值，并筛选出最大值
result = max(33, 45, 12, 78, 99)
print(result) # 99

# min 函数，获取容器中的最小值，返回值是：最小值。
# 备注：min 函数的使用方式与注意点与 max 函数一样，只不过 min 函数返回的是最小值
nums = [23, 11, 32, 30, 17]
result = min(nums)
print(result) # 11

# sum 函数，对容器中的数据进行求和（元素只能是数值不能是字符串或者字符）。
nums = [10, 20, 30, 40, 50]
result = sum(nums)
print(result) # 150