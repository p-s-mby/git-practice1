
def remove_some_letters(arr):
    letters_to_rm = ['A', 'B', 'C', 'D', 'M', 'N']

    new_word = ‘’
    for word in arr:
        for l in word:
            if l.upper() not in letter_to_rm and ord(l) < 87 and str.isalnum(l):
                new_word += l
                if len(new_word) > 7:
                    raise Exception("TooLong Error")
    return new_word
print(remove_some_letters([‘BED’]))
print(remove_some_letters([‘CLOSET’]))

