from Fraction import Fraction
__author__ = 'Hunt Blanchat'


class MixedFraction (Fraction):

    def __init__(self, top, bottom=1):
        """ Initializes num and den after reducing top / bottom
        by their gcd by invoking super.

        Adds fields whole and n, initialized to 0.
        If num > den, assigns the quotient to whole and the remainder to n.
        :param top: numerator
        :param bottom: denominator
        """
        super().__init__(top, bottom)
        self.whole = 0
        self.n = 0
        if self.num >= self.den:
            self.whole = self.num // self.den
            self.n = self.num % self.den

    def __str__(self):
        """ String representation of this fraction.

        Empty strings are used in place of 0.
        :return: whole num / den :: num / den :: whole
        """
        if self.whole == 0:
            return super().__str__()
        elif self.n == 0:
            return str(self.whole)
        return '{} {}/{}'.format(str(self.whole), str(self.n), str(self.den))

    def __add__(self, other):
        """ Adds this fraction to the input parameter (also a
        Fraction (possibly a MixedFraction).

        :param other Fraction or MixedFraction
        :return MixedFraction(n, d)
        """
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        return MixedFraction(n, d)

    def __sub__(self, other):
        """ Subtracts the input parameter (also a
        Fraction (possibly a MixedFraction) from this fraction.

        :param other Fraction or MixedFraction
        :return MixedFraction(n, d)
        """
        n = self.num * other.den - self.den * other.num
        d = self.den * other.den
        return MixedFraction(n, d)

    def __pow__(self, exp):
        """ Multiplies this fraction by itself exp times.

        :param exp: the exponent to be applied
        :return: MixedFraction(n, d) after exponentiation
        """
        f = super().__pow__(exp)
        return MixedFraction(f.num, f.den)

    def __mul__(self, other):
        """  Multiplies other by self and returns a MixedFraction object

        :param other: the Mixed or Fraction self is being multiplied by
        :return: MixedFraction(n, d)
        """
        n = self.num * other.num
        d = self.den * other.den
        return MixedFraction(n, d)

    def __truediv__(self, other):
        """  Divides self by other and returns a MixedFraction object

        :param other: the Mixed or Fraction self is being divided by
        :return: MixedFraction(n, d)
        """
        n = self.num * other.den
        d = self.den * other.num
        return MixedFraction(n, d)

    @classmethod
    def from_string(cls, string):
        """ takes a string as an input and returns a MixedFraction object

        :param string: inputted string
        :return: MixedFraction
        """
        if len(string.strip()) == 1:
            return cls(int(string), 1)
        elif string.find(' ') == -1:
            line = string.strip().split('/')
            numerator = int(line[0])
            denominator = int(line[1])
            return cls(numerator, denominator)
        elif string.strip().find(' ') != -1:
            line = string.strip().split(' ')
            numerator = int(line[0]) * int(line[1][line[1].find('/') + 1:]) + int(line[1][:line[1].find('/')])
            denominator = int(line[1][line[1].find('/') + 1:])
            return cls(numerator, denominator)
        return cls(0)


def main():
    fraction_list = ['330/287', '50 330/287', '1808/287', '27/3']
    new_fraction_list = []
    fraction_sum = MixedFraction(0)
    for x in range(len(fraction_list)):
        if x != 3:
            new_fraction_list.append(MixedFraction.from_string(fraction_list[x]))
            fraction_sum += MixedFraction.from_string(fraction_list[x])
        else:
            new_fraction_list.append(Fraction.from_string(fraction_list[x]))
            fraction_sum += Fraction.from_string(fraction_list[x])
    holder = ''
    holder += '{:} = {:}'.format(' + '.join('{:}'.format(f) for f in new_fraction_list), fraction_sum)
    print(holder)
    for item in new_fraction_list:
        holder = ''
        top = Fraction.factor_fraction(item)[0]
        bottom = Fraction.factor_fraction(item)[1]
        if len(bottom) != 0:
            holder += '{:} = ({:}) / ({:})'.format(item, ' * '.join('{:}'.format(f) for f in top),
                                                   ' * '.join('{:}'.format(a) for a in bottom))
        else:
            holder += '{:} = ({:}) '.format(item, ' * '.join('{:}'.format(f) for f in top))
        print(holder)


if __name__ == '__main__':
    main()