
__author__ = 'Hunt Blanchat'


def sieve(n=int(1e7)):
    """ Builds a list of primes in the range n

    :param n: upper bound
    :return: reverse ordered list of primes less than n
    """
    multiples = set()
    primes = [2]
    for i in range(3, n+1, 2):
        if i not in multiples:
            primes.append(i)
            multiples.update(f for f in range(i*i, n+1, i))
    return primes[::-1]


def largest_prime_factor(n, primes):
    """ Returns the largest prime factor in the list primes

    :param n: upper bound
    :param primes: list of prime numbers
    :return: largest prime factor in list primes or -1 if none
    """
    for i in primes:
        if n % i == 0:
            return i
    return -1


def prime_factors(n, primes):
    """ Returns the prime factorization of a number using the primes in list prime

    :param n: number to find prime factorization
    :param primes: list to pull primes from
    :return: prime factorization of number n
    """
    factors = [largest_prime_factor(n, primes)]
    r = n
    i = 0
    while factors[i] > 0:
        r = r // factors[i]
        i += 1
        factors.append(largest_prime_factor(r, primes))
    check = 1
    for item in factors:
        check *= item
    if check != -n:
        factors.insert(0, -n//check)
    return factors[0:-1]


def display_factors(n, factlist):
    """

    :param n: number that is being factored
    :param factlist: list of prime factors
    :return: string containing comments on factors
    """
    out = ''
    if n > 1e14:
        out += 'Warning: {:,d} is too large to guarantee complete accuracy in finding all the prime factors.\n'.format(n)
    if factlist[0] == n:
        out += '{:,d} is prime'.format(n)
    else:
        out += '{:,d} = {:s}'.format(n, " * ".join('{:,d}'.format(f) for f in factlist  ))
        verifier = 1
        for item in factlist:
            verifier *= item
        if verifier == n:
            out += '\n'+len('{:,d}'.format(n))*' '+' = {:,d} Check'.format(n)
        else:
            out += '\n'+len('{:,d}'.format(n))*' '+' = Oopsy'
    return out


def main():

    primes_list = sieve()
    print('The number of prime numbers < 10,000,000 is', format(len(primes_list), ',d'), 'the largest of which is',
          format((primes_list[0]), ',d'))
    outfile = open('primeFactOut.txt', 'w')
    outfile.write(('The number of prime numbers < 10,000,000 is '+format(len(primes_list), ',d')+' the largest of which is' + format((primes_list[0]), ',d')))
    for line in open('data1.dat', 'r'):
        line = int(line.strip())
        factors_list = prime_factors(line, primes_list)
        print(display_factors(line, factors_list))
        outfile.write((display_factors(line, factors_list)+'\n'))
    outfile.close()


if __name__ == '__main__':
    main()