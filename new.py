# Simple Python program (no input)

name = "Md Frahan"
numbers = [1, 2, 3, 4, 5]

print(f"Hello, {name}!")

for n in numbers:
    print(f"{n} squared is {n ** 2}")

print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")
