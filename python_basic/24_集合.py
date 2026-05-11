'''集合特点
1. 无序：集合中的元素没有固定顺序，无法通过下标访问。
2. 不重复：集合会自动去重，同一个元素只会保留一份。
3. 分为两种：可变集合合（set）和不可变集合（forzenset）。
4. 集合中的元素必须是不可变类型（如：数字、字符串、元组、不可变集合）。
5. 集合支持：并集、交集、差集、对称差集等数学操作。
集合是可以去重的数据容器，当只关心元素是否存在，而不在乎顺序的时，首选集合。
'''
# 可变集合与不可变集合
s1 = {1, 2, 3}
s2 = frozenset({1, 2, 3})
print(type(s1),s1)
print(type(s2),s2)
# 集合的增删
s1 = {1, 2, 3}
# 增加一个元素
s1.add(4)
print(s1)
# 批量增加可迭代对象数据
s1.update({4, 5})
print(s1)
# 删除一个指定元素，删除不存在的元素报错
s1 = {1, 2, 3}
s1.remove(1)
print(s1)
# 删除一个指定元素，删除不存在的元素不会报错
s1 = {1, 2, 3}
s1.discard(4)
print(s1)
# 从集合中删除任意一个元素，返回值是被删除的元素
s1 = {1, 2, 3}
result = s1.pop()
print(s1,result)
# 清空集合
s1 = {1, 2, 3}
s1.clear()
print(s1)
# 改
# 使用 add + remove 的组合，来实现修改的效果
s1 = {10, 20, 30, 40, 50}
s1.remove(20)
s1.add(66)
print(s1)
# 查：集合不能通过下标去读取元素，但能通过 【成员运算符】去查看集合中是否包含指定元素
# 由于成员运算符适用于所有数据容器，所以我们会等所有数据容器都讲完以后，再说成员运算符
s1 = {10, 20, 30, 40, 50}
# s1[0] # 此行报错，因为集合不能通过下标访问元素
# 先提前感受一下成员运算符
result = 20 not in s1
print(result)
'''
集合常用方法
'''
# 集合A.difference(集合B)：
# 作用：找出集合A中，不同于集合B的元素（集合A 与 集合B 都不变，返回的是一个新的集合）
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
result = s1.difference(s2)
print(s1)
print(s2)
print(result)
# 集合A.difference_update(集合B)：
# 作用：从集合A中，删除集合B中存在的元素（集合A会被修改，集合B不会）
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
s1.difference_update(s2)
print(s1)
print(s2)
# 集合A.union(集合B)：
# 作用：合并两个集合，集合A 和 集合B 都不变，返回的是一个新的集合
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
result = s2.union(s1)
print(s1)
print(s2)
print(result)
# 集合A.issubset(集合B)：
# 作用：判断集合A是否为集合B的子集
# 如果 集合A的所有元素都在集合B中，那就返回True，否则返回False
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
s3 = {30, 40, 50}
result = s3.issubset(s1)
print(result)
# 集合A.issuperset(集合B)：
# 作用：判断集合A是否是集合B的超集
# 如果集合A中，包含了集合B中的所有元素，那就返回True，否则返回False
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
s3 = {30, 40, 50}
result = s1.issuperset(s3)
print(result)
# 集合A.isdisjoint(集合B)：
# 作用：
# 如果没有交集，返回True；只要有一个公共元素，就返回False
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
s3 = {80, 90}
result = s1.isdisjoint(s2)
print(result)
'''
集合的数学运算
'''
s1 = {10, 20, 30, 40, 50, 60}
s2 = {40, 50, 60, 70, 80, 90}

# 并集
result = s1 | s2
print(result)

# 交集
result = s1 & s2
print(result)

# 差集
result = s1 - s2
print(result)

# 对称差集,除去两者都有的之外的
result = s1 ^ s2
print(result)
'''
集合的遍历
'''
# 不能使用while循环
s1 = {10, 20, 30, 40, 50, 60}
# 集合可以使用for循环遍历
for item in s1:
    print(item)