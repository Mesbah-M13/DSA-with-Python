''' LeetCode 283. Move Zeroes '''

nums = [0,1,0,3,12,0,7]

'''Brute Force --> ⚓ '''
end_zero_at_end =[]
num_beginning =[]

for i in nums:
    if i == 0:
        end_zero_at_end.append(i)
    else:
        num_beginning.append(i)
result = num_beginning + end_zero_at_end

print(result)

'''Optimized Solution --> Using 2 pointers '''