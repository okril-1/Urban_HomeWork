
def test (*num):
    global a
    a = 1+b
    return a


b = test(2)
print('a',a)


