
def next():
    a = int(input())
    b = int(input())
    c = int(input())
    if a < 31 and (b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12):
        print(a+1, b, c)
    elif a == 31 and (b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10):
        print(1, b+1, c)
    elif a < 30 and (b == 4 or b == 6 or b == 9 or b == 11):
        print(a+1, b, c)
    elif a == 30 and (b == 4 or b == 6 or b == 9 or b == 11):
        print(1, b+1, c)
        
    elif a == 31 and b == 12:
        print(1, 1, c+1)

    elif a == 28 and b == 2 and c % 4 == 0 and c % 100 != 0:
        print(a+1, b, c)
    elif a == 28 and b == 2:
        print(1, b+1, c)

next()
