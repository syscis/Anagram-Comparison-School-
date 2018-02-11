from primeFactorization import prime_factors, sieve
__author__ = 'Hunt Blanchat'


class Fraction:

    def __init__(self, top, bottom=1):
        """ Constructor for MixedFraction.
        Initializes num and den after reducing top / bottom by their gcd.
        :param top: numerator
        :param bottom: denominator
        """
        g = self.gcd(top, bottom)
        self.num = top // g
        self.den = bottom // g

    @staticmethod
    def gcd(m, n):
        """ Euclid's Division Algorithm to find the greatest common denominator (gcd)
        of two integers.
        <http://people.uncw.edu/tompkinsj/133/proofs/quotientRemainderTheorem.htm>
        :param m: an int
        :param n: an int
        :return: the greatest common denominator of m and n
        """
        while m % n != 0:
            m, n = n, m % n
        return n

    def __str__(self):
        """ String representation of this fraction.
        :return: 'num / den'
        """
        return '{}/{}'.format(str(self.num), str(self.den))

    def __add__(self, other):
        """ Adds this fraction to the input parameter (also a Fraction or FixedFraction
        (possibly a MixedFraction). For the MixedFraction case,
        Fraction is moved to second operand so
        MixedFraction handles the addition (arithmetic promotion is required).
        :param other a Fraction, FixedFraction, or MixedFraction
        :return Fraction(n, d)
        """
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        return Fraction(n, d)

    def __pow__(self, exp):
        """ Multiplies this fraction by itself exp times.
        :param exp: the exponent to be applied
        :return: Fraction(n, d) after exponentiation
        """
        n = self.num ** exp
        d = self.den ** exp
        return Fraction(n, d)

    def __truediv__(self, other):
        """  Divides self by other and returns a Fraction object

        :param other: the Fraction self is being divided by
        :return: Fraction(n, d)
        """
        n = self.num * other.den
        d = self.den * other.num
        return Fraction(n, d)

    def __sub__(self, other):
        """  Subtracts other from self and returns a Fraction object

        :param other: the fraction being subtracted from self
        :return: Fraction(n, d)
        """
        n = self.num * other.den - self.den * other.num
        d = self.den * other.den
        return Fraction(n, d)

    def __mul__(self, other):
        """  Multiplies other by self and returns a Fraction object

        :param other: the fraction self is being multiplied by
        :return: Fraction(n, d)
        """
        n = self.num * other.num
        d = self.den * other.den
        return Fraction(n, d)

    def __eq__(self, other):
        """  Checks if self and other are equal

        :param other: Fraction being checked against self
        :return: Boolean
        """
        n = self.num * other.den
        d = self.den * other.num
        if n - d == 0:
            return True
        return False

    def __ne__(self, other):
        """   Checks if self and other are not equal

        :param other: Checks if self and other are not equal
        :return: Boolean
        """

        n = self.num * other.den
        d = self.den * other.num
        if n - d == 0:
            return False
        return True

    def __lt__(self, other):
        """  Checks if self is less than other

        :param other: the Fraction being compared to self
        :return: Boolean
        """
        n = self.num * other.den - self.den * other.num
        if n < 0:
            return True
        return False

    def __gt__(self, other):
        """  Checks if self is greater than other

        :param other: the Fraction being compared to self
        :return: Boolean
        """
        n = self.num * other.den - self.den * other.num
        if n > 0:
            return True
        return False

    def __le__(self, other):
        """  Checks if self is less than or equal to other

        :param other: Fraction being compared to self
        :return: Boolean
        """
        n = self.num * other.den - other.num * self.den
        if n <= 0:
            return True
        return False

    def __ge__(self, other):
        """ Checks if self is greater than or equal to other

        :param other: Fraction being compared to self
        :return: Boolean
        """
        n = self.num * other.den - other.num * self.den
        if n >= 0:
            return True
        return False

    @classmethod
    def from_string(cls, string):
        """ Takes a string as an input and returns a Fraction object

        :return: Fraction object
        """
        if len(string.strip()) == 1:
            return cls(int(string), 1)
        elif len(string.strip()) > 1:
            line = string.strip().split('/')
            numerator = int(line[0])
            denominator = int(line[1])
            return cls(numerator, denominator)
        return cls(0)

    @staticmethod
    def factor_fraction(self):
        primes = sieve(max(self.num, self.den))
        top = prime_factors(self.num, primes)
        bottom = prime_factors(self.den, primes)
        return top, bottom


def main():
    pass


if __name__ == '__main__':
    main()