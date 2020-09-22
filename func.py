

def x(z):
    y = ['A', 'B', 'C', ‘D’]
    d = ‘’
    for word in z:
	for letter in word:
    	    if letter not in y and ord(letter) < 87:
                d += letter
    return d
print(x(‘BED’))
print(x(‘CLOSET’))