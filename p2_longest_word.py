def LongestWord(sen):
    no_s = ''
    word_list = []
    longest = ''

    # take out special characters
    for i in sen:
        if i.isalpha():
            no_s += i
        elif i.isalnum():
            no_s += i
        elif i == ' ':
            no_s += i

    # make word_list
    word_list = no_s.split()

    # find longest_word
    longest = max(word_list, key=len)
    return longest


# keep this function call here
print LongestWord(raw_input())
