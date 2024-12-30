def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))
