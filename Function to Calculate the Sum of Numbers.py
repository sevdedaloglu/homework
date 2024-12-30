def calculate_sum(numbers):
    return sum(numbers)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("The sum of the numbers is:", calculate_sum(numbers))
