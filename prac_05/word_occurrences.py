"""
Word Occurrences
Estimate: 25 minutes
Actual:    minutes
"""

text = input("Text: ")
word_counts = {}

words = text.split()
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word, count in word_counts.items():
    print(f"{word} : {count}")