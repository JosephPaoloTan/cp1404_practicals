word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    number_of_times = word_to_count.get(word, 0)
    word_to_count[word] = number_of_times + 1

words = list(word_to_count.keys())
words.sort()

maximum_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{maximum_length}}: {word_to_count[word]:1}")