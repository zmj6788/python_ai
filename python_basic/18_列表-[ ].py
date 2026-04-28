'''列表特点
1. 可存放不同类型的元素。
2. 元素是有序存储的（正索引、负索引）。
3. 列表中的元素允许重复。
4. 元素是允许修改的（增、删、改、查、其他操作）。
5. 长度不固定，可以随着操作自动调整大小。
列表是最常用的数据容器，当遇到要“存储一批数据”的场景时，首选列表。
'''
# 定义有内容的列表
list1 = [1, 2, 3, 4, 5]
# 列表中存列表，可以当作二维坐标
list2 = [[1,2],[3,4],[5,6]]
print(list1)
print(list2)
# 列表的增删改查
# 查询，通过下标方式
print(list2[0][1]) # 2
print(list2[-1])  # [5,6]
print(list2[1:])  # [[3, 4], [5, 6]]
print(list2[:-2])  # [[1, 2]]
# 更改列表指定序列的字面量
list2[1] = [2,2]
print(list2)
# 增加到列表的尾部
list1.append(23)
print(list1)
# 增加到列表的指定位置
list1.insert(0,100)
print(list1)
# 增加可迭代数据到列表尾部
list1.extend([7,8,9])
print(list1)
# 删除指定位置的字面量,并返回删除的值
result= list1.pop(6)
print(list1)
print(result)
# 删除查询到的第一个字面量
list1.remove(1)
print(list1)
# 删除指定序列的字面量
del list1[0]
print(list1)
# 清空列表
list1.clear()
print(list1)
# 备注：所有的列表方法，都只作用于“当前层”的元素（浅层操作），不会自动进入嵌套的“里层”结构中。
# 列表.index(值)，查找指定元素在列表中第一次出现的下标，返回值是元素下标。
fruits = ['香蕉', '苹果', '橙子', '香蕉']
result = fruits.index('香蕉')
print(result)  # 0
# 列表.count(值)，统计某个元素在列表中出现的次数，返回值是：元素出现的次数
nums = [10, 20, 10, 30, 10, 40, [10, 10, 10]]
result = nums.count(10)
print(result)  # 3
# 列表.reverse()，反转列表（会改变原列表），无需参数，无返回值
nums = [23, 11, 32, 30, 17, [6, 7, 8, 9]]
nums.reverse()
print(nums)  # [[6, 7, 8, 9], 17, 30, 32, 11, 23]
# 列表.sort(reverse=布尔值)，对列表排序（从小到大，会改变原列表），reverse 用于控制排序方式，无返回值。
# 都是数字，则按照数字的大小顺序进行排序。
nums = [23, 11, 32, 30, 17]
nums.sort(reverse=True)
print(nums)  # [32, 30, 23, 17, 11]
# 既有数字，又有字符串，那就会报错。
nums = [23, 11, 32, 30, 17, '尚硅谷']
# nums.sort()
print(nums) # [23, 11, 32, 30, 17, '尚硅谷']
# 都是字符串，则按照字符串的 Unicode 编码大小进行排序
msg_list = ['北京', '北硅谷', '北好']
msg_list.sort()
print(msg_list)  # ['北京', '北好', '北硅谷']
print(ord('京'), ord('好'), ord('硅'))  # ['北京', '北好', '北硅谷']

# 使用for循环遍历列表（通过enumerate函数，同时获取下标（索引值）和元素）
# enumerate 的 start 参数，可以让计数从指定值开始（改变的是循环时的“编号”，不是真正的索引值）
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
score_list = [62, 50, 60, 48, 80, 20, 95]
for index, item in enumerate(score_list, start=5):
    print(index, item)
print(list(enumerate(score_list)))

