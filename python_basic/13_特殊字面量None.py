# None是一个特殊的字面量，它表示：空值 / 无值 / 无意义。
msg = None

# None 的类型是 NoneType。
print(type(msg))

# None 转为布尔值是 False。
print(bool(msg))
if not msg:
    print('你好')

# 不能参与数学运算，也不能与字符串拼接。
# result1 = msg + 1
# result1 = msg + 'hello'

# 变量是盛放东西的“瓶子”。
# 字面量是直接往瓶子里倒的“水”或“果汁”
# 之所以叫这个名字，是因为它的值完全取决于它的字面长相