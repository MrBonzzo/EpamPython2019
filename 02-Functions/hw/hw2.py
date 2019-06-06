def atom(var=None):

    def get_value():
        nonlocal var
        return var or 0

    def set_value(arg=None):
        nonlocal var
        var = arg or 0
        return var

    def process_value(*functions):
        nonlocal var
        for func in functions:
            var = func(var)
        return var

    def delete_value():
        nonlocal var
        del var
    return get_value, set_value, process_value, delete_value

if __name__ == '__main__':
    get_, set_, proc_, del_ = atom(10)
    assert get_() == 10
    assert set_() == 0
    assert get_() == 0
    assert set_(15) == 15
    assert get_() == 15
    # (15 + 1)**2 = 256
    assert proc_(lambda x: x+1, lambda x: x**2) == 256
    del_()
    try:
        assert get_()
    except NameError as e:
        print(f'"{e}" while calling del_() after get_()')
