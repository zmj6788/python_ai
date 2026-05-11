class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self,msg):
        print(f'我是{self.name}，我想说:{msg}')
# 定义一个Student类（子类、派生类）， 继承自Person类（父类、超类、基类）
class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        # 在子类中，有两种方式去调用父类的初始化方法，来实现对继承属性：name, age, gender 初始化操作
        # 方式1（更推荐）
        super().__init__(name, age, gender)
        # 方式2
        # Person.__init__(self, name, age, gender)
        # 子类独有的属性，需要自己手动完成初始化
        self.stu_id = stu_id
        self.grade = grade

    def study(self):
        print(f'我叫{self.name}，我在努力的学习，争取做到{self.grade}年级的第一名')

    # 方法重写：当子类中定义了一个与父类中相同的方法，那么子类中的方法就会“覆盖”父类的方法
    def speak(self, msg):
        super().speak(msg)
        print(f'我是学生，我的学号是{self.stu_id}，我正在读{self.grade}，我想说：{msg}')
# 创建Student类的实例对象
s1 = Student('李华', 16, '男', '2025001', '初二')
print(s1.__dict__)
print(type(s1))
# 查找speak方法的过程：1.实例自身(s1) => 2.Student类 => 3.Person类
s1.speak('你好')
print(s1.__dict__)
# 查找study方法的过程：1.实例自身(s1) => 2.Student类 => 3.Person类
s1.study()
'''
方法重写
当子类中定义了一个与父类中相同的方法，那么子类中的方法就会“覆盖”父类的方法
'''
s1 = Student('李华', 12, '男', '2025001', '初二')
# 查找speak方法的过程：1.实例自身(s1) => 2.Student类 => 3.Person类
s1.speak('好好学习')
'''
两个常用方法
isinstance() 和 issubclass()
'''
p1 = Person('张三', 18, '男')
s1 = Student('李华', 12, '男', '2025001', '初二')

# 方法1：isinstance(instance, Class)，作用：判断某个对象是否为指定类或其子类的实例
print(isinstance(s1, Student))
print(isinstance(p1, Person))
print(isinstance(s1, Person))
print(isinstance(p1, Student))

# 方法2：issubclass(Class1, Class2)，作用：判断某个类是否是另一个类的子类
print(issubclass(Student, Person))
print(issubclass(Person, Student))

'''
多重继承
'''
# 所谓多重继承，就是一个类，可以同时继承多个父类
# 定义一个Person类
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}')

# 定义一个Worker类
class Worker:
    def __init__(self, company):
        self.company = company
    def do_work(self):
        print(f'我在{self.company}做兼职')

# 定义一个Student类，继承自：Person类、Worker类
class Student(Person, Worker):
    def __init__(self, name, age, gender, stu_id, grade, company):
        Person.__init__(self, name, age, gender)
        Worker.__init__(self, company)
        self.stu_id = stu_id
        self.grade = grade
    def study(self):
        print(f'我在很努力的学习，争取做{self.grade}年级的第一名')

# 创建Student实例对象
s1 = Student('张三', 18, '男', '2025001', '初二', '麦当劳')
print(s1.__dict__)
s1.speak()
s1.do_work()
s1.study()

# 类的__mro__属性：用于记录属性和方法的查找顺序
# 通过实例去查找属性或方法时，会现在实例自身上寻找，如果没有，就按照__mro__中所记录的顺序去查找
print(Student.__mro__)

'''
进阶多重继承（super() + **kwargs 完美接力方式）
'''
class Person:
    # 使用 **kwargs 接收并传递多余的参数（比如 company）
    def __init__(self, name, age, gender, **kwargs):
        self.name = name
        self.age = age
        self.gender = gender
        super().__init__(**kwargs)  # 加上括号，并把剩余参数传给下一个类（Worker）

    def speak(self):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}')


class Worker:
    def __init__(self, company, **kwargs):
        self.company = company
        super().__init__(**kwargs)  # 加上括号，继续把接力棒传给 object

    def do_work(self):
        print(f'我在{self.company}做兼职')


class Student(Person, Worker):
    def __init__(self, name, age, gender, stu_id, grade, company):
        # super() 不需要传 self，只需要按照 MRO 顺序传递 Person 需要的参数以及 company
        super().__init__(name=name, age=age, gender=gender, company=company)
        self.stu_id = stu_id
        self.grade = grade

    def study(self):
        print(f'我在很努力的学习，争取做{self.grade}年级的第一名')


# 创建Student实例对象
s1 = Student('张三', 18, '男', '2025001', '初二', '麦当劳')
print(s1.__dict__)
s1.speak()
s1.do_work()
s1.study()

# 打印 MRO 顺序
print("Student的MRO顺序为:", Student.__mro__)