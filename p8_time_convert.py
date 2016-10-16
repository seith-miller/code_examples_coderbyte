def TimeConvert(num):
    h = ''
    m = ''

    h = str(num / 60)
    m = str(num % 60)

    # code goes here
    return h + ':' + m


# keep this function call here
print TimeConvert(raw_input())
