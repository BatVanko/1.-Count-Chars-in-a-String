text = input()
count_chars = dict()

chars = [w for w in text if w != " "]

for char in chars:
    if char not in count_chars.keys():
        count_chars[char] = 0
    count_chars[char] += 1

for char in count_chars.keys():
    print(f"{char} -> {count_chars[char]}")
