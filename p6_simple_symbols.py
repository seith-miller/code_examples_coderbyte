def SimpleSymbols(str):
    out = 'true'
    str_l = len(str)

    if str[-1].isalpha() or str[0].isalpha():
        return 'false'

    for i in range(0, str_l - 1):
        if str[i].isalpha():
            if str[i - 1] != '+' or str[i + 1] != '+':
                out = 'false'
                return out

    return out


# keep this function call here
print SimpleSymbols(raw_input())
