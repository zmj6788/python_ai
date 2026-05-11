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