"""
Word Occurrences
Estimate: 25 minutes
Actual:   35 minutes
"""

text = input("Text: ")
word_counts = {}

words = text.split()
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word in sorted(word_counts):
    print(f"{word} : {word_counts[word]}")