def dzielenie(x, y, calkowitoliczbowe=False):
    """
    Oblicza iloraz dwóch liczb.

    >>> dzielenie(2,4)
    0.5
    >>> dzielenie(3, 4, True)
    0
    >>> dzielenie(4, 16, False)
    0.25
    >>> dzielenie(4, 16, True) # niepoprawny wynik
    0.25
    """
    if y == 0:
        if x >= 0:        return float("Inf")
        else:             return -float("Inf")
    if calkowitoliczbowe: return x // y
    else:                 return x  / y

if __name__ == "__main__":
    import doctest
    doctest.testmod()
