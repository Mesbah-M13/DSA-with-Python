nums = [0,0,1,1,1,2,2,3,3,4]

# remove_duplicates = set(nums)
# nums = list(remove_duplicates)
# print(remove_duplicates,type(remove_duplicates))
# print(nums)

# n= len(nums)
# r = 1

# for i in range(1,n):
#     if nums[i] != nums[i-1]:
#         nums[r] = nums[i]
#         r += 1
# print(r)
        

























nums = [0,0,1,1,1,2,2,3,3,4]

n = len(nums)
r = 1

for l in range(1,n):
    if nums[l] != nums[r-1]:
        nums[r] = nums[l]
        r += 1

print(r)


