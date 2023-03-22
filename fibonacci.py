# Get the value of n from the user
n = int(input("Enter the number of terms you want to generate: "))

# Initialize the first two terms of the sequence
a,b = 0,1

# Generate the sequence up to the nth term
for i in range(n):
    print(a)
    a,b = b,a+b


