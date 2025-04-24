'''
26. Remove Duplicates from Sorted Array

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

nums = [0,0,1,1,1,2,2,3,3,4]

# remove_duplicates = set(nums)
# nums = list(remove_duplicates)
# print(remove_duplicates,type(remove_duplicates))
# print(nums)

n= len(nums)
r = 1

for i in range(1,n):
    if nums[i] != nums[i-1]:
        nums[r] = nums[i]
        r += 1
print(r)


