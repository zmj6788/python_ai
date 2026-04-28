# 定义函数（设置参数默认值）
def greet(name, gender, age, height, msg='你好'):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')
    print(f'我想说：{msg}')

# 设置参数默认值的参数后必须都设置有参数默认值
# 调用函数
greet('张三', '男', 18, 172)
greet('张三', '男', 18, 172, 'hello')
greet('张三', '男', 18, 172, msg='hello')

# 示例 print的end默认值是\n
print('你好',end='\n')
print('你好')