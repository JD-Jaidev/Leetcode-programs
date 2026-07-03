# PALINDROME NUMBER - RETURN BOOLEAN IF NUMBER IS PALINDROME OR NOT

# BRUTE FORCE APPROACH : Convert to string, reverse the string and compare with origial string.
# TIME COMPLEXITY : O(n) Converting to a string and reversing both take time proportional to the number of digits.
# SPACE COMPLEXITY : O(n) A new reversed string is created.

num = 12321
def palindromeNumber(num):
    s = str(num)

    if num < 0:
        print(False)
    if s == s[::-1]:
        print(True)
    else:
        print(False)

palindromeNumber(num)

# OPTIMISED APPROACH : Rverse the intger mathematically using %,//. Then compare reversed number with original.
# TIME COMPLEXITY : O(log n) The number of digits in an integer n is approximately log₁₀(n).
# SPACE COMPLEXITY : O(1) Only a few integer variables are used.

num = 12321
def palindromeNumber(num):
    if num < 0:
        print(False)

    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    print(original == reverse)

palindromeNumber(num)
