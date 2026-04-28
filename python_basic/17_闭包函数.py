'''
闭包的三个基本特征
在 Python 中，要形成闭包，必须满足以下三个条件：
必须有嵌套函数（函数内部定义函数）。
内部函数引用了外部函数的变量（非全局变量）。
外部函数返回内部函数本身（不是返回函数的结果）
'''
def add(x: int):
    def inner(y: int) -> int:
        return x + y
    return inner

# 使用方式
add_five = add(5)
print(add_five(10))  # 输出 15
print(add_five(10))  # 输出 15
# 累加版本
def make_adder(x: int):
    def adder(y: int) -> int:
        # 由于 Python 的保护机制，在内部函数修改外部变量需要使用 nonlocal 关键字。
        nonlocal x  # 告诉 Python：我要改外面那个 x 的值
        x = x + y   # 执行赋值操作
        return x
    return adder

accumulate = make_adder(5)
print(accumulate(10))  # 5 + 10 = 15
print(accumulate(10))  # 15 + 10 = 25 (值变了！)
print(accumulate(10))  # 25 + 10 = 35