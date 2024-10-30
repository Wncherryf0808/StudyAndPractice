"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
"""
def removeElements(nums, val):
# 注意： nums移除元素后，相关列表内容及长度会发生变化
    count = 0
    for i in range(len(nums)):
        if val in nums:
            nums.remove(val)
            count += 1

    return count, nums


print(removeElements([0,1,2,2,3,0,4,2], 2))