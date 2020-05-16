def number_game(n):
    if n % 3 == 0 :
        if n % 5 == 0 :
            return "FizzBuzz"
        else:
            return "Fizz"

    elif n % 5 == 0:
        return "buzz"

    else:
        return n

n = int(input("enter a number : ") )
for n in range(1, n):
    print(number_game(n))
