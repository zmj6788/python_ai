# 定义一个Person类（类名通常使用：大驼峰写法）
from datetime import datetime


class Person:
    # max_age、planet 他们都是类属性，类属性是保存在类身上的
    # 类属性可以通过类访问，也可以通过实例访问
    # 类属性通常用于保存：公共数据
    max_age = 120
    planet = '地球'
    # 说明：当一个函数被定义在了类中时，那这个函数就被称为：方法。
    # __init__方法：初始化方法，主要作用：给当前正在创建的实例对象添加属性
    # __init__方法收到的参数：当前正在创建的实例对象（self）、其它的自定义参数
    # 当我们以后编写代码去创建Person类实例的时候，Python会自动调用__init__方法
    def __init__(self, name, age, gender):
        # 通过实例.属性名 = 值定义在实例身上的属性，称为：实例属性
        # 实例属性只能通过实例访问，不能通过类访问
        # 每个实例都有自己【独一份的】实例属性，各个实例之间是互不干扰的
        self.name = name
        self.gender = gender
        # 使用类属性限制age的最大值
        if age <= Person.max_age:
            self.age = age
        else:
            print(f'年龄超出范围了，已经将年龄设置为最大值：{Person.max_age}')
            self.age = Person.max_age
    # 下面的speak方法、run方法，都保存在类身上，但他们主要是供实例调用，所以他们都叫：实例方法
    # 自定义方法（给实例添加行为）
    # speak方法收到的参数是：调用speak方法的实例对象（self）、其它参数
    # speak方法只有一份，保存在Person类身上的，所有Person类的实例对象，都可以调用到speak方法
    def speak(self,msg):
        print(f'我叫{self.name}，我今年{self.age}岁了，我想说{msg}')

    # 自定义方法（给实例添加行为）
    def run(self, distance):
        print(f'{self.name}疯狂的奔跑了{distance}米')

    # 使用 @classmethod 装饰器装饰过的方法，就叫：类方法，类方法保存在类身上的
    # 类方法收到的参数：当前类本身（cls）、自定义的参数
    # 因为收到了cls参数，所以类方法中是可以访问类属性的
    # 类方法通常用于实现：与类相关的逻辑，例如：操作类级别的信息、一些工厂方法
    @classmethod
    def change_planet(cls, value):
        cls.planet = value

    @classmethod
    def create(cls, info_str):
        # 从info_str中获取到有效信息
        name, year, gender = info_str.split('-')
        # 获取当前年份
        current_year = datetime.now().year
        # 计算年龄
        age = current_year - int(year)
        # 创建并返回一个Person类的实例对象
        return cls(name, age, gender)

    # 静态方法
    # 使用 @staticmethod 装饰过的方法，就叫：静态方法，静态方法也是保存在类身上的
    # 静态方法只是单纯的定义在类中，它不会收到：self、cls参数，它收到的参数都是自定义参数
    # 由于静态方法没有收到：self、cls参数，所以其内部不会访问任何：类和实例相关的内容
    # 静态方法通常用于定义：与类相关的工具方法
    @staticmethod
    def is_adult(year):
        # 获取当前的年份
        current_year = datetime.now().year
        # 计算年龄
        age = current_year - year
        # 返回结果（成年True，未成年False）
        return age >= 18

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6] + '********' + idcard[-4:]

'''
创建实例化对象
'''
p = Person('ZMJ',18,'男')
# 查看实例对象的某一个属性
print(p.age)
# 通过 实例.__dict__ 可以查看实例身上的所有属性
print(p.__dict__)
# 实例创建完毕后，依然可以通过 实例.属性名 = 值 去给实例追加属性
p.address = '北京昌平宏福科技园'
print(p.__dict__)
# 通过type函数，可以查看某个实例对象，是由哪个类创建出来的
print(type(p))
'''
自定义方法
'''
# 调用自定义方法
# 当执行p.speak()的时候，查找speak方法的过程：1.实例对象自身(p1)  =>  2.实例的“缔造者”的身上(Person)
print(Person.__dict__)
p.speak('你好')
# 验证一下上述的查找过程
def speak():
    print('巴拉巴拉巴拉巴拉巴拉')
p.speak = speak
print(Person.__dict__)
print(p.__dict__)
p.speak()
'''
类属性
'''
# 验证类属性是保存在类身上的
print(Person.__dict__)
# 验证一下：类属性可以通过类访问，也可以通过实例访问
print(Person.max_age)
print(p.max_age)  # 查找max_age的过程：1.实例自身(p1)  => 2.实例的“缔造者”(Person)
# 注意点：进行【实例.属性名 = 值】操作时，只会对实例自身的属性起作用，不会影响类属性
p.planet = '火星'
print(Person.__dict__)
print(p.__dict__)
'''
实例方法
'''
# 创建Person类的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)
# 通过实例调用实例方法
p1.speak('你好')
p1.run(300)
# 通过类去调用实例方法(能调用，但不推荐)
Person.run(p2, 100)
'''
类方法
'''
print(Person.__dict__)
Person.change_planet("火星")
print(Person.__dict__)
p = Person.create("悟空-2003-男")
print(p.__dict__)
# 注意点：类方法，也能通过实例调用到，但是非常不推荐
p4 = p1.create('李华-2003-女')
print(p4.__dict__)
'''
静态方法
'''
# 验证一下：静态方法也是保存在类身上的
print(Person.__dict__)

# 静态方法需要通过类去调用
# result = Person.is_adult(2015)
# print(result)
# result2 = Person.mask_idcard('212101198802030028')
# print(result2)

# 注意点：通过实例也能调用到静态方法，但非常不推荐
p1 = Person('张三', 18, '男')
res = p1.mask_idcard('212101198802030028')
print(res)