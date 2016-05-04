#!/opt/anaconda3/bin/python3

def dzielenie(x, y, calkowitoliczbowe=False):
    """
    Liczy iloraz dwoch liczb
    """
    if y==0:
        if x>=0:
            return float("Inf")
        else:
            return -float("Inf")
    if calkowitoliczbowe:
        return x//y
    else:
        return x/y

if __name__ == '__main__':
    # testy jednostkowe
    assert dzielenie(2,2) == 1
    assert dzielenie(3,9) == 3/9
    for i in range(1, 100):
        assert dzielenie(3,i) == 3/i
    for i in range(1, 100):
        assert dzielenie(3,i, True) == 3//i
    assert dzielenie(5,0) == float('Inf')
    assert dzielenie(-5,0) == float('Inf') #bledny test
