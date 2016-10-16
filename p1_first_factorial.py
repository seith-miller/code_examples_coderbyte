def FirstFactorial(num):

    for i in range(num - 1, 1, -1):
        num = num * i

    return num


# keep this function call here
print FirstFactorial(raw_input())
