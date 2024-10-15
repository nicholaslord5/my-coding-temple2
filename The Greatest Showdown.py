# Task 1: Identify the Greatest
# Write a Python program that asks the user to enter three numbers.
# Your code should then identify and print out the largest number among the three.

# Expected Outcome: If we provide the numbers 3, 3, and 4,
# it should print out that "The smallest number is 3. The largest number is 4."

a, b, c = input("Enter three numbers.").split()
smallest = min(a, b, c)
largest = max (a, b, c)
print("The smallest number is {}. The largest number is {}".format(smallest, largest))

