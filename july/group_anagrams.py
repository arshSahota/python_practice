words = ["eat", "tea", "tan", "ate", "nat", "bat"]

def is_anagram(words):
    result = {}

    for word in words:
        key = "".join(sorted(word))

        if key not in result:
            result[key] = []

        result[key].append(word)

    return list(result.values())

print(is_anagram(words))