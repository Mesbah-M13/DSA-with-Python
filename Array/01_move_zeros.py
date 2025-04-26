''' LeetCode 283. Move Zeroes '''

nums = [0,1,0,3,12,0,7]

'''Brute Force --> ⚓ '''
zero_at_end =[]
num_beginning =[]

for i in nums:
    if i == 0:
        zero_at_end.append(i)
    else:
        num_beginning.append(i)
result = num_beginning + zero_at_end

#print(result)

'''Optimized Solution --> Using 2 pointers '''

l = 0 # left
for r in range(len(nums)): # r = right
    if nums[r] != 0:
        nums[l],nums[r] = nums[r],nums[l]
        l +=1
    
print([nums])
