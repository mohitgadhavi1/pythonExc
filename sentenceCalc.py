sentence = input("Enter a Sentence: ")

digits = 0
upper_letters = 0
lower_letters = 0

for char in sentence:
    if char.isdigit():
        digits += 1
    elif char.isupper():
        upper_letters += 1
    elif char.islower():
        lower_letters += 1

print("Digits:", digits)
print("Uppercase letters:", upper_letters)
print("Lowercase letters:", lower_letters)