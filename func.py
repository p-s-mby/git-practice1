

def x(z):
    y = ['A', 'B', 'C', ‘D’]
    d = ‘’
    for r in z:
        if r not in y and ord(r) < 87:
            d += r
    return d
print(x(‘BED’))
print(x(‘CLOSET’))