# 两数之和
# 给定一个整数数组 nums 和一个目标值 target，返回两数之和的下标
# 解法：哈希表，一次遍历

def twoSum(nums,target):
    d={}
    for i,num in enumerate(nums):
        completement=target-num
        if completement in d:
            return [d[completement],i]
        d[num]=i
     return []
if_name_=="_main_":
     print(twoSum([2,7,11,15],9))
