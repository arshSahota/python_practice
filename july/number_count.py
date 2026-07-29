nums = [4, 7, 1, 4, 9, 7, 2, 4]

def num_freq(nums):
    num_fre = {}

    for num in nums:
            num_fre[num] = num_fre.get(num, 0) + 1
    for num, fre in num_fre.items():
        if fre == 1:
            return num

print(num_freq(nums))