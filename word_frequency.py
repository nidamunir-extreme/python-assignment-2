from collections import Counter
import re

def word_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)  # Find all words
        word_count = Counter(words)
    return word_count


word_freq = word_frequency('test.txt')
print(word_freq)  # Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
