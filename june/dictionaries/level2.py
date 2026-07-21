sentence = input("Enter a sentence: ")

def total_words(sentence):
    sentence = sentence.split()
    return len(sentence)

def longest_word(sentence):
    sentence = sentence.split()
    longest = sentence[0]
    for word in sentence:
        if len(word) > len(longest):
            longest = word
    return longest

def shortest_word(sentence):
    sentence = sentence.split()
    shortest = sentence[0]
    for word in sentence:
        if len(word) < len(shortest):
            shortest = word
    return shortest

print("Total words: ", total_words(sentence))
print("Longest word: ", longest_word(sentence))
print("Shortest word: ", shortest_word(sentence))