"""
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，
使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。
然后返回 nums 中唯一元素的个数。
"""
def removeDuplicates(nums):

    if not nums:
        return 0

    index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[index]:
            index += 1

            nums[index] =nums[i]
    return index + 1