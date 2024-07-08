numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

is_prime = []
not_primes = []
primes = numbers

while numbers[0] == 0 or numbers[0] == 1:
    numbers.remove(numbers[0])

for i in numbers:
    for g in range(len(numbers)):
        if g != 0 and g != 1 and g != i:
            if i % g == 0:
                not_primes.append(i)
                break
print(not_primes)
for i in not_primes:
    primes.remove(i)
    for g in range(len(numbers)):
        if g != 0 and g != 1:
            if i==g:

                continue

print(primes)
