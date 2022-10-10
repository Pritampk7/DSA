data = [0, 3, 4, -1 - 5]
max_sum = 0

current_value = data[0]
for item in data:
    if current_value < 0:
        current_value = 0
    current_value += item
    max_sum = max(max_sum, current_value)

print(max_sum)
