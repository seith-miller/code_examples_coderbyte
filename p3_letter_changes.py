def LetterChanges(str):
    new_str = ''
    vowels = 'aeiou'

    # replace letters with next letter
    for i in str:
        if i.isalpha():
            new_str += chr(ord(i) + 1)
        else:
            new_str += i

    # make vowles upper
    out = ''.join(l.upper() if l in vowels else l for l in new_str)

    # code goes here
    return out


# keep this function call here
print LetterChanges(raw_input())
