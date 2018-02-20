sum_of_the_squares = sum(i ** 2 for i in range(1, 101))
square_of_the_sum = sum(j for j in range(1, 101)) ** 2
print(square_of_the_sum - sum_of_the_squares)
