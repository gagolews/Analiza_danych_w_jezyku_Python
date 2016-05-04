#!/opt/anaconda3/bin/python3

if __name__=='__main__':
    import sys
    if len(sys.argv) != 4:
        print("USAGE: %s dzialanie argument1 argument2" % sys.argv[0])
        sys.exit()
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    print( {
    "+": a+b,
    "-": a-b,
    "*": a*b,
    "/": a/b
    }[sys.argv[1]])