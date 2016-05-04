def kwadrat(x):
    """
    Liczy kwadrat danej liczby.
    >>> kwadrat(2)
    4
    >>> kwadrat(3)
    9
    >>> kwadrat(4) # to sie "wywali"
    9
    """
    return x**2

if __name__ == '__main__':
    # testy jednostkowe
    assert kwadrat(2) == 4
    assert kwadrat(3) == 9
    for i in range(0, 100):
        assert kwadrat(i) == i**2

    # itd.
    import doctest
    doctest.testmod()
    # doctest - troche automatyzacji
