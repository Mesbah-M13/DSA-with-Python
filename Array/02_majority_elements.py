''' LeetCode 169. Majority Element'''
# Solve 1: Using HashMap 

'''
list1 =[4,4,3,3,4]

count_elem = {}

def find_majority_element(nums):
    for element in list1:
        count_elem[element] = count_elem.get(element,0) + 1
        # print(count_elem)

    for key,value in count_elem.items():
        if value > len(list1)//2:
            return key
        
print(find_majority_element(list1))

'''
nums = [2,2,1,1,1,2,2,3,3,3,3,3,3]

canditate = nums[0]
count = 1

for num in nums[1:]:
    if canditate == num:
        count += 1
    else:
        if count == 0:
            canditate = num
            count = 1
        else:
            count -= 1
print(canditate)