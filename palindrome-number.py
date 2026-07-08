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

# OPTIMISED APPROACH : Reverse the intger mathematically using %,//. Then compare reversed number with original.
# TIME COMPLEXITY : O(n) The while loop runs once for each digit of num, stripping off one digit (num % 10) and building the reversed number each iteration.
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

# ANOTHER TYPE APPROACH
# TIME COMPLEXITY : Takes O(n) time to convert the number to a string.
# SPACE COMPLEXITY : str(x) creates a new string of length n, which takes O(n), an extra space.

x=12321
def palindrome_number1(x):
    s=str(x)
    l=0
    r=len(s)-1
    while l<=r:
        if s[l]==s[r]:
            l+=1
            r-=1
        else:
            return False
    return True
print(palindrome_number1(x))
