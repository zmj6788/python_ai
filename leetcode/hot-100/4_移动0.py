from typing import List


def moveZeroes(nums: List[int]) -> None:
    '''
    解题思路：既然只需要将是0的元素移到列表末尾
    那么如果为0，删除列表中一个为0的然后在列表的末尾增加一个0
    '''
    for n in nums:
        if n == 0:
            nums.remove(0)
            nums.append(0)
    print(nums)
nums = [0,1,0,3,12]
moveZeroes(nums)
def moveZeroesPro(nums: List[int]) -> None:
    '''
    解题思路：第一个不是0的放在列表中第一个位置以此类推
    最后将其他空余位置更改为0
    '''
    head = 0
    for n in nums:
        if n != 0:
            nums[head] = n
            head += 1
    for i in range(head, len(nums)):
        nums[i] = 0
    print(nums)
nums = [0,1,0,3,12]
moveZeroesPro(nums)
def moveZeroesProMax(nums: List[int]) -> None:
    '''
    解题思路：双指针，i指向不是0的元素。i0指向不是零元素应该互换的元素
    第一个不是0的位置的元素与第一个位置的元素互换，以此类推
    标准双指针解法。i 是快指针负责探路，i0 是慢指针指向“已处理好的非零序列的末尾”。
    只要 i 遇到非零数，就和 i0 位置的元素交换
    '''
    i0 = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[i], nums[i0] = nums[i0], nums[i]
            i0 += 1

nums = [0,1,0,3,12]
moveZeroesProMax(nums)