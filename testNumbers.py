import random
import time

__author__ = 'Hunt Blanchat'


def sequential_search(alist, item):
    """ Searches iteratively through a list for an item

    :param alist: inputted list
    :param item: item being searched for
    :return: boolean depending on whether item is found or not
    """
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

    return found


def better_find_helper(alist, element, start, end):
    """

    :param alist: sorted list
    :param element: item searched being searched for
    :param start: lower bound on search indices
    :param end: upper bound on search indices
    :return: returns boolean depending on whether item is found
    """
    if start > end:
        return False
    middle = (start + end) // 2
    if alist[middle] == element:
        return True
    elif alist[middle] > element:
        return better_find_helper(alist, element, start, middle - 1)
    else:
        return better_find_helper(alist, element, middle + 1, end)


def better_find(alist, element):
    """ Helper function for binary search, simplifies input to two parameters instead of four

    :param alist: sorted list
    :param element: item being searched for
    :return: call of betterFindHelper which eventually returns boolean
    """
    return better_find_helper(alist, element, 0, len(alist) - 1)


def main():
    print(" N Linear Sort & Binary Search Binary Search only")
    out_file = open('TestNumberTimes.csv', 'w')
    out_file.write(' N, Linear, Sort & Binary Search, Binary Search only\n')
    for n in range(500000, 5000001, 500000):
        random_list = [random.randrange(0, 2*n) for x in range(n)]
        for i in range(len(random_list)):
            if i not in random_list:
                notx = i
                break

        start1 = time.clock()
        sequential_search(random_list, notx)
        stop1 = time.clock()
        time1 = stop1 - start1

        start2 = time.clock()
        random_list.sort()
        better_find(random_list, notx)
        stop2 = time.clock()
        time2 = stop2 - start2

        start3 = time.clock()
        better_find(random_list, notx)
        stop3 = time.clock()
        time3 = stop3 - start3

        print('{:10,}\t{}\t{}\t{}'.format(n, time1, time2, time3))
        out_file.write('{:10},{},{},{}'.format(n, time1, time2, time3)+'\n')
    out_file.close()


if __name__ == '__main__':
    main()