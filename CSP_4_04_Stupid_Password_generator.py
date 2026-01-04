"""
Problem: Stupid Password Generator
Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid” passwords" that consist of the following 5 characters:

Character 1: a digit from 1 to n.
Character 2: a digit from 1 to n.
Character 3: a small letter from the first l letters of the Latin alphabet.
Character 4: a small letter from the first l letters of the Latin alphabet.
Character 5: a digit from 1 to n, greater than the first 2 digits.
Input Data
The input is read as arguments and consists of two integers: n and l within the range [1 … 9].Screenshot 2025-10-07 at 10.53.33 AM.png

Output Data
Return a list of all "stupid" passwords in alphabetical order.
"""

def stupidPassword(n: int, l: int):
    passwords = []
    for digit1 in range(1, n + 1):
        for digit2 in range(1, n + 1):
            for i in range(l):
                letter1 = chr(ord('a') + i)
                for j in range(l):
                    letter2 = chr(ord('a') + j)
                    bigger = max(digit1, digit2)
                    for digit5 in range(bigger + 1, n + 1):
                        password = str(digit1) + str(digit2) + letter1 + letter2 + str(digit5)
                        passwords.append(password)
#alphabetical stuff
    passwords.sort()

    return passwords


