def find_maximum(numbers):
    return max(numbers)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("The maximum value is:", find_maximum(numbers))
