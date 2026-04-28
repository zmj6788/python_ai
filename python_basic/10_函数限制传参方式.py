# /的前面使用位置参数，*后面使用关键字参数，两者同时存在，*不能再/前
def Hello(name,/,gender,*,age,phone):
    print(f'我是{name}，我是{gender}生，我今年{age}岁，我的联系方式是{phone}')
Hello('悟空','男',age=18,phone=123456)