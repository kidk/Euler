__author__ = 'Samuel'

def check(value):
    if value % 1 != 0:
        return False;
    if value % 2 != 0:
        return False;
    if value % 3 != 0:
        return False;
    if value % 4 != 0:
        return False;
    if value % 5 != 0:
        return False;
    if value % 6 != 0:
        return False;
    if value % 7 != 0:
        return False;
    if value % 8 != 0:
        return False;
    if value % 9 != 0:
        return False;
    if value % 10 != 0:
        return False;
    if value % 11 != 0:
        return False;
    if value % 12 != 0:
        return False;
    if value % 13 != 0:
        return False;
    if value % 14 != 0:
        return False;
    if value % 15 != 0:
        return False;
    if value % 16 != 0:
        return False;
    if value % 17 != 0:
        return False;
    if value % 18 != 0:
        return False;
    if value % 19 != 0:
        return False;
    if value % 20 != 0:
        return False;

    return True

value = 1

while not check(value):
    value += 1

print (value)