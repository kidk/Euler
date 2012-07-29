__author__ = 'Samuel'

#
# WRONG (SLOW)
#

primes = []
last = 0
primes.insert(last, 2)

def NextPrime():
    global last, primes

    number = primes[last]
    found = False

    while not found:
        number += 1

        found = True
        for x in range(2, number - 1):
            if (number % x == 0):
                found = False

    last += 1
    primes.insert(last, number)

def GetPrime(location):
    global last, primes

    if (last < location):
        for i in range (last, location):
            NextPrime()

    return primes[location]

goal = 600851475143

print(GetPrime(1000))

