"""
5. Fizzbuzz With a Twist

Print numbers 1–50. But:

Multiples of 3 → "Fizz"
Multiples of 5 → "Buzz"
Multiples of both → "FizzBuzz"
If the number itself contains the digit 3 → "Sneaky"
If BOTH rules apply (e.g. multiple of 3 AND contains a 3) → "FizzSneaky"

"""
for num in range(51):
    num += 1

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0 and '3' in str(num):
        print("FizzSneaky")
    elif '3' in str(num):
        print("Sneaky")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
