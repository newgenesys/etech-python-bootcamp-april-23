import doctest


def compute_total_amount_with_compound_interest(p, r, n):
    """ Return the total amount due for a loan after borrowing amount p, for n months with an interest rate of r%
    >>> compute_total_amount_with_compound_interest(10000, 5, 36)
    11576.25
    """
    result = p * ((1 + (r / 100)) ** (n / 12))

    return round(result, 2)


def list_high_low_avg(items):
    """ Return the average of the highest and lowest numbers in a list, items
    >>> list_high_low_avg([1, 2, 3, 4, 5, 6, 7, 8, 9])
    5.0
    >>> list_high_low_avg([4,5])
    4.5
    >>> list_high_low_avg([10, 22])
    16.0
    """
    lowest = min(items)
    highest = max(items)

    output = (lowest + highest) / 2

    return output


if __name__ == '__main__':
    doctest.testmod(verbose=True)
