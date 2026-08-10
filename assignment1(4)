p = input("Enter paragraph: ")

words = p.split()

print("Total words:", len(words))

print("Unique words:", len(set(words)))

longest = max(words, key=len)
shortest = min(words, key=len)

print("Longest word:", longest)
print("Shortest word:", shortest)

print("Words appearing more than once:")

for word in set(words):
    if words.count(word) > 1:
        print(word)
