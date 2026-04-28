def add(*ns :int()) -> int:
    """
    计算两个数相加的结果
    :param ns:可变位置参数，接受位置参数为元组
    :return:元组中元素累加的结果
    """
    result = 0
    for n in ns:
        result += n
    return result
print(add(1, 2, 3, 4))
# 三个引号加回车生成说明文档格式