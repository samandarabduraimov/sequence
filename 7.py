def square_of_numbers(n, numbers):
    squares = [x ** 2 for x in numbers]
    return squares

n = int(input("Foydalanuvchidan sonlar sonini kiriting: "))
numbers = list(map(int, input(f"{n} ta sonni kiriting: ").split()))

result = square_of_numbers(n, numbers)
print("Output:", result)
