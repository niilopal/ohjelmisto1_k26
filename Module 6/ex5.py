nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 0
def filter_even_numbers(nums, n):
    for i in nums:
        if nums[n] % 2 != 0:
            nums.remove(i)
        n += 1
print(f'Original list: {nums}')
filter_even_numbers(nums, n)
print(f'List with even numbers only: {nums}')