# and具备“逻辑短路”能力，以下代码中包含3/0这种错误代码，但最终没有报错。
from operator import truediv

print(False and 3 / 0)  # False，前面错误，后面不执行
print(3 > 9 and 3 / 0)  # False
# and返回的不一定是布尔值，它返回的是某个参与计算的值本身，
# and会先看左边，如果左边是“假”，就直接返回左边，否则返回右边；
# 若参与and运算的值不是布尔值，那 Python 会自动转为布尔值，然后再进行逻辑操作。
print(2 - 2 and True) # 0
print('' and True)
print(True and 8 / 2)  # 4.0
print(3 + 3 and 3 * 4) # 12
# or同样具备“逻辑短路”的能力，以下代码中包含3/0这种错误代码，但最终没有报错。
print(True or 3 / 0)  # True，前面正确，后面不执行
print(3 > 0 or 3 / 0)  # True
# or返回的也不一定是布尔值，它返回的是参与计算的值本身，
# or会先看左边，如果左边为“真”，就直接返回左边，否则返回右边；
# 若参与or运算的值不是布尔值，那 Python 会自动转为布尔值，然后再进行逻辑操作。
print(7 - 2 or False)    # 5
print('你好' or '尚硅谷') # 你好
print(False or 8 / 2)	 # 4.0
print(2 - 2 or 3 * 4)    # 12
# not返回的值，一定是布尔值！
print(not 0) 	  # True
print(not 3 > 2)  # False
print(not 9 // 4) # False
print(not 'abc')  # False
print(not '')  # True