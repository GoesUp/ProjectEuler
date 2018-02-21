maximum_value = 0
number_that_produces_the_highest_value = 1
dict = {}
for i in range(1, 10 ** 6):
    counter = 1
    temp = i
    while i is not 1:
        if i < temp:
            counter += dict[i]
            i = 1
        else:
            if i % 2 == 0:
                i = i // 2
            else:
                i = 3 * i + 1
        counter += 1
    dict[temp] = counter
    if counter > maximum_value:
        maximum_value = counter
        number_that_produces_the_highest_value = temp

print(number_that_produces_the_highest_value)
