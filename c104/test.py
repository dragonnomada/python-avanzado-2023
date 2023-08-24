import sum_of_squares

result = 0

for _ in range(100_000):
    n = 1_000
    result += sum_of_squares.sum_of_squares(n) / 1_000_000_000

print(f"The sum of squares from 1 to {n} is: {result}")
