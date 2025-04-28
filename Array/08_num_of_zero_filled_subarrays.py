'''348. Number of Zero-Filled Subarrays

    https://leetcode.com/problems/number-of-zero-filled-subarrays/description/

'''
nums = [1,3,0,0,2,0,0,4]

current = total = 0

for num in nums:
    if num == 0:
        current += 1
        total += current
    else:
        current = 0
print(total)