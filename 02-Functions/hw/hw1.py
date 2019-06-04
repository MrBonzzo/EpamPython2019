def letters_range(*args, **kwargs):
    if len(args) == 1:
        letters = [chr(x) for x in range(ord('a'), ord(args[0]))]
    elif len(args) == 2:
        letters = [chr(x) for x in range(ord(args[0]), ord(args[1]))]
    elif len(args) == 3:
        letters = [chr(x) for x in range(ord(args[0]), ord(args[1]), args[2])]
    for k in kwargs:
        letters[letters.index(k)] = str(kwargs[k])
    return letters


if __name__ == '__main__':
    temp = letters_range('b', 'w', 2)
    assert(temp == ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v'])
    temp = letters_range('g')
    assert(temp == ['a', 'b', 'c', 'd', 'e', 'f'])
    temp = letters_range('g', 'p')
    assert(temp == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'])
    temp = letters_range('g', 'p', **{'l': 7, 'o': 0})
    assert(temp == ['g', 'h', 'i', 'j', 'k', '7', 'm', 'n', '0'])
    temp = letters_range('p', 'g', -2)
    assert(temp == ['p', 'n', 'l', 'j', 'h'])
    temp = letters_range('a')
    assert(temp == [])
