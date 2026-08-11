# Python program to calculate the sum of two numbers

def sum_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        total = sum_two_numbers(num1, num2)
        print("The sum is:", total)
    except ValueError:
        print("Please enter valid numbers.")
