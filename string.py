# 1.
s = "hello"
print(s[::-1])

# 2.
s = "education"
vowels = "aeiou"
count = sum(1 for ch in s if ch.lower() in vowels)
print("Vowel count:", count)

# 3.
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))

# 4.
sentence = "this is a test this is"
words = sentence.split()
counts = {word: words.count(word) for word in set(words)}
print(counts)

# 5.
def caesar_cipher(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

print(caesar_cipher("abc", 3))

# 6.
import re
email = "test@example.com"
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
print(bool(re.match(pattern, email)))