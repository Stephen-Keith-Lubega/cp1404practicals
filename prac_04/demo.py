from operator import index

# names = ["Keith", "Alan", "Marlin", "Tom"]
# name_to_display = int(input(f"Name number up to {len(names)}: "))
# try:
#     print(names[name_to_display - 1])
# except IndexError:
#     print("Invalid number")


string = "Hello"
print(string[0]) # 'H'
for character in string:
    print(character.upper(), end="-")
print(len(string))
print(string)


from operator import itemgetter
score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
new_data = input("New data separated by a ,(eg Matin, 6): ")
print(new_data)
split_data = new_data.split(sep=",")
print(split_data)
split_data[1] = int(split_data[1])
print(split_data)
score_pairs.append(split_data)
score_pairs.sort(key=itemgetter(1), reverse=True)
print(score_pairs)

# text = "This is a sentence"
# long_words = [word of word in text.split() if len(word)>3]



name = "Alice"
score = 95

# Left-aligned string in 10 characters
print(f"{name:>10}")