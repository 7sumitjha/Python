def number_game(n):
    if n % 3 == 0 and  n % 5 == 0:
        return str(n) +" fizzbuzz"

    elif n % 5 == 0:
        return str(n) + " buzz"

    elif n % 3 == 0 :
        return str(n) + " fizz"

    else:
        return n


n = int(input("enter a number : ") )
for n in range(1, n):
    print(number_game(n))
