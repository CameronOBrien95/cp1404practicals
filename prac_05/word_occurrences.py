"""
CP1404/CP5632 Practical
Count word occurrences in a string
"""
word_count = {}
sentence = input("Text: ")
for word in sentence.split(" "):
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
longest_word = max((len(word) for word in word_count))
print(longest_word)
for word in sorted(word_count):
    print("{:{}} : {}".format(word, longest_word, word_count[word]))