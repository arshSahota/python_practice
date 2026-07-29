nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):

    seen = {}

    for i, x in enumerate(nums):
        need = target - x

        if need in seen:
            return [seen[need], i]

        seen[x] = i
        
print(two_sum(nums, target))