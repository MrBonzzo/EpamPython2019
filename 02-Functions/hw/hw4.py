from inspect import getsource
from inspect import signature


def modified_func(func, *fixated_args, **fixated_kwargs):

    def inner(*fixed_args, **fixed_kwargs):
        args = list(fixated_args + fixed_args)
        kwargs = fixated_kwargs.copy()
        kwargs.update(**fixed_kwargs)
        return func(*args, **kwargs)
    inner.__name__ = f'func_{func.__name__}'
    inner.__doc__ = f'A func implementation of {func.__name__}\n'
    inner.__doc__ += f'with pre-applied arguments being:\n'
    sig = signature(func).bind(*fixated_args, **fixated_kwargs).arguments
    for s in sig:
        inner.__doc__ += f'{s} = {sig[s]}\n'
    inner.__doc__ += f'\nsource_code:\n'

    # если вызывать inspect.getsource() для built-in функций, то TypeError
    inner.__doc__ += getsource(func)
    return inner


def arg_kwarg_func(a, b, c=81, *args, **kwargs):
    print(a, b, c, args, kwargs)


if __name__ == '__main__':
    md_func = modified_func(arg_kwarg_func, 5, 3, 4, 342, kw_0=0, kw_1=1)
    print(f'{md_func.__name__}\n')
    print(f'{md_func.__doc__}\n')
    md_func()
