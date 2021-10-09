key = input()
word = input()
count = 0

for index_i in range(len(key) - len(word) + 1):
    len_word = len(word)
    new_word = key[index_i:index_i + len_word]
    has_equals = False
    for index_j in range(len_word):
        if new_word[index_j] == word[index_j]:
            has_equals = True
            break
    if not has_equals:
       count += 1

print(count)
