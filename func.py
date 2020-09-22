

def x(z):
    y = ['A', 'B', 'C', 'D', 'M', 'N']
    d = ''
    for r in z:
        if r not in y and ord(r) < 87:
            d += r
    return d
print(x(‘BED’))
print(x(‘CLOSET’))