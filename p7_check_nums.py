def CheckNums(num1, num2):

    if num2 > num1:
        return 'true'
    elif num2 == num1:
        return '-1'

    else:
        return 'false'

    return 'error'


# keep this function call here
print CheckNums(raw_input())
