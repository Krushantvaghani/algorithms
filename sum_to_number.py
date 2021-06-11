"""
    Gives an array of integers, return indies of the two numbers
    such that they add to specific range

    You may assume that each input would have exactly one soluction,
    and you may not use the same element twice

    Example: 
        Given nums = [2,7,12,15] target = 9,

        Because nums[0] + num[7] = 9 output
        return [0,1] 
"""


# Create one function
def twoSum(nums: "List[int]", target:"int")->"List[int]":
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            return [dic[num],i]
        else:
            dic[target - num] = i


if __name__== "__main__":
    arr = [3,2,4]
    target = 6
    res = twoSum(arr,target)
    print("Output show for index",res)