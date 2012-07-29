__author__ = 'Samuel'

value = 1
previous = 0
result = 0
while value < 4000000:
    print(value)


    if value % 2 == 0:
        result += value

    previous_temp = value
    value += previous
    previous = previous_temp


print(result)
