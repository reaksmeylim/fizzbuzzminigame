# Reaksmey Lim 25/11/2019
# FizzBuzz Mini Game in Python
for fizzbuzz in range(1, 101): #Range from 1 to 100 exclude 101

    # number divisible by 3 and 5 must be divible by 15
    # print "FizzBuzz"
    if fizzbuzz % 15 == 0:
        print("FizzBuzz")
        continue

    # number divisible by 3
    # print "Fizz"
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue

    # number divisible by 5
    # print "Buzz"
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue

    # print output
    print(fizzbuzz)
