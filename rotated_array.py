"""
    Rotate an array of n element to right by k step

    For example, with n = 7 and k = 3,
    the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

    Note:
    Try to come up as many solutions as you can,
    there are at least 3 different ways to solve this problem.
"""

def rotateOnyByOne(number, e):
    num = len(number)
    for i in range(e):
        temp = number[num-1]
        for j in range(num-1,0,-1):
            number[j] = number[j-1]
        number[0] = temp
        

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    reverse(nums, 0, n - k - 1)
    reverse(nums, n - k, n - 1)
    reverse(nums, 0, n - 1)


def reverse(array, a, b):
    while a < b:
        array[a], array[b] = array[b], array[a]
        a += 1
        b -= 1