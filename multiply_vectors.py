
vector1 = [2, 4, 5]
vector2 = [2, 3, 6]

vector1_len = len(vector1)

new_list = []

for num in range(vector1_len):
    product = vector1[num] * vector2[num]
    new_list.append(product)

print(new_list)

