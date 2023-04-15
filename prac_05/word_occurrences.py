# Adrianto Hartono
# 14347930

"""
Word Occurrences
Estimate: 30 minutes
Actual: 40 minutes
"""

user_input= str(input("Text: "))
text = user_input.split()
length = 0
words = {}

for word in text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
        if len(word) > length:
            length = len(word)

maximum_word = max(len(words) for word in words)
sorted_word = sorted(words.items())

for name, count in sorted_word:
    print(f"{name:{maximum_word}} : {count}")
