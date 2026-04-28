from typing import List
# sorted()可以对列表，元组，字符串，集合，字典，可迭代的可排序的数据进行排序
# 返回排序后的列表，不更改元数据
# reverse=True：实现倒序（从大到小）。
# key 函数：这是它的“灵魂”。你可以告诉 Python 按什么标准排。
# 按绝对值排：sorted([-5, 2, -1], key=abs)
# 按长度排：sorted(["apple", "ok", "banana"], key=len)
def groupAnagrams( strs: List[str]) -> List[List[str]]:
    # 创建一个字典，键是排序后的单词，值是包含原单词的列表
    idx = {}

    for s in strs:
        # 1. 将单词排序作为哈希表的键 (eat -> aet)
        # sorted(s) 返回新列表 ['a', 'e', 't']，不修改原列表，需要 join 成字符串做键
        # 可以接受任何可迭代对象（包括列表、元组、字符串、字典、集合等）
        # s.sort(),直接排序原列表，没有返回值
        # 列表（list）专属的方法，只能用于列表
        key = "".join(sorted(s))
        print(type(s)) # str
        print(type(sorted(s))) # list
        print(type(key)) # str

        # 2. 如果键不在字典里，初始化一个空列表
        if key not in idx:
            idx[key] = []

        # 3. 将原单词加入对应的组
        idx[key].append(s)

    # 4. 返回字典中所有的值（即分组后的列表）
    return list(idx.values())
# if key not in idx:相当于 if idx.get(key) is None
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
