import string
import random
import time

__author__ = 'Hunt Blanchat'


def random_string(size):
    """ generates a random string of lowercase letters of length size

    :param size: length of randomly generated string
    :return: string of lowercase letters with length size
    """
    return ''.join(random.choice(string.ascii_lowercase) for x in range(size))


def make_anagram(s):
    """ generates an anagram from inputted string s

    :param s: inputted string to be made into an anagram
    :return: string of len(s) that is an anagram of s
    """
    temp = s
    t = ''
    while temp != '':
        i = random.randrange(0, len(temp))
        t += temp[i]
        temp = temp[:i] + temp[(i+1):]
    return t


def anagram_solution1(s1, s2):
    """ Takes two strings as inputs and creates a list of the string being checked.
    That list is then compared to the characters in the first string, s1. If a match
    is found then the list value is set to None.

    :param s1: string
    :param s2: string being checked against s1
    :return: boolean
    """
    alist = list(s2)

    pos1 = 0
    stillok = True

    while pos1 < len(s1) and stillok:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillok = False

        pos1 = pos1 + 1

    return stillok


def anagram_solution2(s1, s2):
    """ Takes two inputted strings, sorts them and then compares them iteratively

    :param s1: string
    :param s2: string being checked against s1
    :return: boolean
    """
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


def anagram_solution4(s1, s2):
    """ Takes two strings as inputs and counts the number of times a specific letter
    appears in each string, then compares those counts.

    :param s1: string
    :param s2: string being checked against s1
    :return: boolean
    """
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillok = True
    while j < 26 and stillok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillok = False

    return stillok


def main():
    out_file = open('anagramSolutionData.csv', 'w')
    out_file.write('N, SolutionS1, SolutionS2, SolutionS4\n')
    for n in range(1000, 10001, 500):
        t = random_string(n)
        s = make_anagram(t)

        start1 = time.clock()
        anagram_solution1(t, s)
        stop1 = time.clock()
        time1 = stop1 - start1

        start2 = time.clock()
        anagram_solution2(t, s)
        stop2 = time.clock()
        time2 = stop2 - start2

        start3 = time.clock()
        anagram_solution4(t, s)
        stop3 = time.clock()
        time3 = stop3 - start3

        out_file.write('{:10},{},{},{}'.format(n, time1, time2, time3)+'\n')
    out_file.close()


if __name__ == '__main__':
    main()