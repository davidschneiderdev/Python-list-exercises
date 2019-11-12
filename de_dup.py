
given_list = ["cat", "dog", "fish", "air", "water", "earth", "fire", "earth", "cat"]

new_list = []

for word in given_list:
    if word not in new_list:
        # print(word)
        new_list.append(word)

print(new_list)

