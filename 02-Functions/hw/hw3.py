counter = 0


def make_it_count(func, counter_name):
    def inner():
        func()
        globals()[counter_name] += 1
    return inner


def my_func():
    print('Do Nothing')


if __name__ == '__main__':
    new_func = make_it_count(my_func, 'counter')
    for i in range(1, 5):
        new_func()
        assert i == counter
