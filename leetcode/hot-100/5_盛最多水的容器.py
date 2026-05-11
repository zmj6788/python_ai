from typing import List


def maxArea(height: List[int]) -> int:
    '''
    解题思路：将盛水容器当做求阴影面积，长 * 宽 最大的就是盛水最多的容器
    '''
    max_area = 0
    for i, v in enumerate(height):
        for j in range(i + 1, len(height)):
            area = (j - i) * min(v, height[j])
            max_area = max(max_area, area)
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


def maxArea(height: List[int]) -> int:
    '''
    解题思路：双指针，分别指向起始和末尾
    移动左指针和右指针中指向元素小的指针向内测移动
    原因移动指针指向大的元素向内部移动总面积一定会变小
    '''
    left, right, max_area = 0, len(height) - 1, 0
    while left < right:
        if height[left] < height[right]:
            max_area = max(max_area, height[left] * (right - left))
            left = left + 1
        else:
            max_area = max(max_area, height[right] * (right - left))
            right = right - 1
    return max_area


print(maxArea([1,1]))
