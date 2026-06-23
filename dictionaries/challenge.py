# def all_unique(lst):
#     freq = {}
#     for item in lst:
#         freq[item] = freq.get(item, 0)+1
    

#     for item in freq:
#         if freq[item] > 1:
#             return False
#         return True

# test_list = [2,2,3,4]
# print(all_unique(test_list))

# #challenge 2

# def count_occurences(lst):
#     freq = {}
#     for item in lst:
#         freq[item] = freq.get(item, 0) + 1

#     return freq

# input = [1, 2, 2, 3, 3, 3]
# print(count_occurences(input))

#challenge 3

def compress_string(s):
    result = ""
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1

    result += s[-1] + str(count)
    return result
    
print(compress_string("aaabbc"))

#challenge 4
# from collections import Counter

# def second_most_frequent(s):
#     freq = {}
#     for char in s:
#         freq[char] = freq.get(char, 0) + 1

#     sorted_items = sorted(freq.items(), key = lambda x:x[1], reverse = True)
#     return sorted_items[1][0]
    
# print(second_most_frequent("success"))

# #challenge 5

# def flatten(lst):
#     result = []

#     for item in lst:
#         for num in item:
#             result.append(num)
#     return result

# input = [[1,2], [3,4], [5]]
# print(flatten(input))

