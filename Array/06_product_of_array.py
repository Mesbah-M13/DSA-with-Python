'''
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/description/

'''
# Method 1 : 

nums = [1,2,3,4]

def productExceptSelf(nums):
    n = len(nums)
    result = []

    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)

    return result
print(productExceptSelf(nums))


# Method 2 : Optimal
'''
nums = [1,2,3,4]

n= len(nums)
result = [1] * n

prefix = 1
for num in range(n):
    result[num] = prefix
    prefix *= nums[num]

postfix = 1
for num in range(n-1,-1,-1):
    result[num] *= postfix
    postfix *= nums[num]

print(result)

'''


'''
range(n-1, -1, -1)
range(start, stop, step)

start = n - 1 → begins from the last index
stop = -1 → the loop will stop just before -1, i.e., stop at 0
step = -1 → it moves backwards (decrementing by 1)

'''