num1 = 0b1001  # 2进制0b开头,不区分大小写
num2 = 0o1001  # 8进制0o开头,不区分大小写
num3 = 0x1cf  # 16进制0x开头,不区分大小写
print(num1, num2, num3)
# 十进制转换其他进制
print(bin(num2))  # 转化为2进制，内部参数可以是任何进制数
print(oct(num1))  # 转化为8进制
print(hex(num1))  # 转化为16进制
# 其他进制转换十进制
print(int('0b1001', 2))  # 2进制转化为10进制
print(int('0o1001', 8))  # 8进制转化为10进制
print(int('0x1cf', 16))  # 16进制转化为10进制
