# 定义函数（使用*args去接收：以*开头定义参数，可变位置参数，args只是大家习惯这么写，当然也可以换成其他变量）
def test1(*args):
    # 此处args的值，是一种新的数据类型，叫：元组，我们下一章就去讲元组
    print(args)

# 调用函数
test1('张三', '男', 18, 172)
# 定义函数（使用**kwargs去接收：以**开头定义参数，可变关键字参数，kwargs只是大家习惯这么写，当然也可以换成其他变量）
def test2(**kwargs):
    # 此处kwargs的值，是一种新的数据类型，叫：字典，我们下一章就去讲字典
    print(kwargs)

# 调用函数
test2(name='张三', gender='男', age=18, height=172)
# 定义函数（同时使用：可变位置参数、可变关键字参数）
def test3(a, b, *args, c='尚硅谷', **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
# 调用函数
test3('张三', '男', '抽烟', '喝酒', age=18, height=172)