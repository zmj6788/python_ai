from typing import List


# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中。
def twoSum(nums: List[int], target: int) -> list[int]:
    for i, v in enumerate(nums):
        for j, w in enumerate(nums):
            if v + w == target:
                return [i, j]
    return []


print(twoSum([2, 7, 11, 15], 9))


def twoSumPro(nums: List[int], target: int) -> list[int]:
    idx = {}  # 创建一个空哈希表（字典），键值对
    for j, x in enumerate(nums):  # x=nums[j]
        if target - x in idx:  # 在左边找 nums[i]，满足 nums[i]+x=target
            return [idx[target - x], j]  # 返回两个数的下标
        idx[x] = j  # 保存 nums[j] 和 j


# if idx.get(target-j) is not None:可以替换 if target - x in idx:
print(twoSumPro([3, 2, 4], 6))
