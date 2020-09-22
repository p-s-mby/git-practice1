

def remove_some_letters(arr):
    letters_to_rm = ['A', 'B', 'C', 'D', 'M', 'N']
    new_word = ‘’
    for word in arr:
        for l in word:
            if l not in letter_to_rm and ord(l) < 87:
                new_word += l
    return new_word
print(remove_some_letters([‘BED’]))
print(remove_some_letters([‘CLOSET’]))

