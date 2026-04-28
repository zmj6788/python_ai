from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if not nums: return 0
    # 用 set 去重且保证 O(1) 查询
    num_set = set(nums)
    max_len = 0
    # 遍历 set 而不是 nums，可以减少重复计算
    for v in num_set:
        # 哨兵：只有 v 是起点时才进入
        # v-1不在字典中存在，说明这里是连续序列的开头
        if (v - 1) not in num_set:
            y = v + 1
            while y in num_set:
                y += 1

            # 直接用变量记录最大值，省去维护一个 longs 列表的内存
            max_len = max(max_len, y - v)
    return max_len


nums = [100, 4, 200, 1, 3, 2, 1]
print(longestConsecutive(nums))
