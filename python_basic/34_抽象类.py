from abc import ABC, abstractmethod

#【抽象类】是一种不能直接实例化的类，它通常作为“规范”，让子类去继承，并实现其中定义的【抽象方法】。

# MustRun类一旦继承了ABC类，那MustRun类就是【抽象类】了
class MustRun(ABC):
    # run方法一旦被@abstractmethod装饰后，就变成了【抽象方法】
    @abstractmethod
    def run(self):
        pass

class Person(MustRun):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def run(self):
        print(f'我叫{self.name}，我在努力的奔跑！')

p1 = Person('张三', 18, '男')
p1.run()
'''
抽象类结合标准多态
'''
# 1. 定义抽象类（规范）
class Shape(ABC):
    @abstractmethod
    def area(self):
        """计算面积，子类必须实现"""
        pass

# 2. 子类实现抽象方法（具体实现）
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

# 3. 多态调用（统一接口）
def print_area(shape: Shape):
    print(f"面积是: {shape.area()}")

print_area(Circle(5))   # 输出: 面积是: 78.5
print_area(Rectangle(3, 4)) # 输出: 面积是: 12

from typing import Protocol
'''
python，Protocol实现类似go中的隐式接口
即你实现了接口的所有方法，你就是这个接口的类型，不需要显示继承
'''
# 定义一个“协议”（接口）
class Drawable(Protocol):
    def draw(self) -> None: ...

# 无需继承，只要结构匹配即可
class Circle:
    def draw(self) -> None:
        print("画一个圆")

class Square:
    def draw(self) -> None:
        print("画一个正方形")

# 多态使用
def render(shape: Drawable):
    shape.draw()

render(Circle())  # 输出: 画一个圆
render(Square())  # 输出: 画一个正方形