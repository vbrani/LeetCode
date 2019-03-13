nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    x = i+1
    for j in range(x,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)
