def sum_of_list(nums):
    sum = 0
    n = 0
    for i in nums:
        sum += nums[n]
        n+=1
    n = 0
    return sum
nums = [1, 2, 3, 4, 5]
sum = sum_of_list(nums)
print('The sum of the numbers in the list is:', sum)