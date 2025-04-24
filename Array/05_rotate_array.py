'''
189. Rotate Array
https://leetcode.com/problems/rotate-array/description/

'''

#  Method - 1 : Using Slicing for
# nums = [1,2,3,4,5,6,7]
nums = [-1,-100,3,99]
k = 2
n = len(nums)
k = k % n

nums[:] = nums[-k:] + nums[:n-k]
print(nums)




'''
nums = [1,2,3,4,5,6,7]
k = 3

def rotate(nums, k):
    n = len(nums)
    k = k % n
    
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse entire array
    reverse(0, n - 1)

    # Step 2: Reverse first k elements
    reverse(0, k - 1)

    # Step 3: Reverse the rest
    reverse(k, n - 1)
    print(f"Step 3: Reverse remaining {n - k} elements => {nums}")

    print(f"\nFinal rotated array: {nums}\n")
    
rotate(nums,k)
'''