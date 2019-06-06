import inspect
import hw1


def modified_func(func, *fixated_args, **fixated_kwargs):

    def inner(*fixed_args, **fixed_kwargs):
        args = list(fixated_args + fixed_args)
        kwargs = fixated_kwargs.copy()
        kwargs.update(**fixed_kwargs)
        return func(*args, **kwargs)
    inner.__name__ = f'func_{func.__name__}'
    inner.__doc__ = f'A func implementation of {func.__name__}\n'
    inner.__doc__ += f'with pre-applied arguments being:\n'
    inner.__doc__ += f'\nfixated_args:\n'
    for fa in fixated_args:
        inner.__doc__ += f'{fa}\n'
    inner.__doc__ += f'\nfixated_kwargs:\n'
    for fkwa in fixated_kwargs:
        inner.__doc__ += f'{fkwa}: {fixated_kwargs[fkwa]}\n'
    inner.__doc__ += f'\nsource_code:\n'
    inner.__doc__ += inspect.getsource(func)
    return inner


if __name__ == '__main__':
    mod_letters_range = modified_func(hw1.letters_range, 'b', 's', d='1', f=0)
    print(mod_letters_range.__name__)
    print(mod_letters_range.__doc__)
    without_args_kwargs = mod_letters_range()
    print(without_args_kwargs)
    with_args_kwargs = mod_letters_range(2, h='1', r='9')
    print(with_args_kwargs)
