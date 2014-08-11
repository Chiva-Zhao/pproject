'''
Created on 11 Aug 2014

@author: cz186008
'''
def median(nums):
    nums = sorted(nums)
    length = len(nums)
    if(length % 2 == 1):
        return nums[int((length -1)/2)]
    else:
        return (nums[int(length/2 -1)] + nums[int(length/2)])/2
print(median([4,5,5,4]))    