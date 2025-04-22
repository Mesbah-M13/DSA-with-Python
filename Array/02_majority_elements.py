''' LeetCode 169. Majority Element'''

nums = [2,1,1,1]

count ={}
def majorityElemnt(nums):
    for num in nums:
        count[num] = count.get(num,0) +1 
        # print(f"Count of each values as key:value",count)

    # for key,value in count.items():
    #     if value > len(nums)//2:
    #         return key
        
# print(majorityElemnt(nums))










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
