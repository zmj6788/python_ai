# 使用bool()将指定内容转为布尔类型
print(bool(1))  # True
print(bool(0))  # False
# Python中除0以外的任何数，转为布尔值后都为 True
print(bool(300))  	# True
print(bool(25.6))  	# True
print(bool(1.8e3))  # True
print(bool(12_000)) # True
print(bool(-10))  	# True
# Python中除空字符串以外的任何字符串，转为布尔值都是 True
print(bool('hello')) # True
print(bool('0'))	 # True
print(bool('18.5'))	 # True
print(bool('-9'))	 # True
print(bool(''))	     # False