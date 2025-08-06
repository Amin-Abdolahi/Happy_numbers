'''
    this program checks if a number is a happy number
A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.
If it enters a cycle which does not include 1, it is not a happy number.
The process of repeatedly replacing a number by the sum of the squares of its digits is called "digit squaring".
The first few happy numbers are: 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100
'''
# step 1: get a number from user
user_number = input("Enter your number: ")
# step 2: Check if a number is a happy number
def is_happy_number(n):
    while n != 1 and n != 4:
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

# step 3: Print the result
if is_happy_number(int(user_number)):
    print(user_number, "is a happy number.")
else:
    print(user_number, "is not a happy number.")
    
print("The process of digit squaring for", user_number, "is as follows:")
n = int(user_number)
while n != 1 and n != 4:
    n = sum(int(digit) ** 2 for digit in str(n))
    print(n)


if __name__ == "__main__" :
    assert is_happy_number(7) == False
    assert is_happy_number(4) == False
    assert is_happy_number(68) == True