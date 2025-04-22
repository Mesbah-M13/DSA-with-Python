nums = [1,2,3,1,1,3]

result = 0
count ={}

for i in nums:
    if i in count:
        result += count[i]
        #print(result)
        count[i] += 1
    else:
        count[i] = 1
print(count)

