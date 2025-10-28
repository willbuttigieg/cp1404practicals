"""
CP1404 Practical
Word Occurrences
Estimate: 25 minutes
Actual:   23 minutes
"""

word_to_occurrences = {}
text = input("Text: ").lower()
words = sorted(text.split())
for word in words:
    word_to_occurrences[word] = word_to_occurrences.get(word, 0) + 1
length_of_longest_word = max(len(words) for words in word_to_occurrences.keys())
for word in word_to_occurrences:
    print(f"{word:{length_of_longest_word}} : {word_to_occurrences[word]}")
