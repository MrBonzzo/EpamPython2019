from functools import reduce
import time


# hw 1:
problem_6 = sum(range(101))**2 - sum(map(lambda x: x**2, range(101)))

problem_9 = [b * c * (1000 - b - c) for c in range(335, 998)
             for b in range(1, c)
             if 0 < (1000 - b - c) < b < c and
             c**2 == b**2 + (1000 - b - c)**2][0]

problem_40 = reduce(lambda a, x: a * x,
                    [int(''.join([str(c) for c in range(200_000)])[10**i])
                     for i in range(7)])

problem_48 = sum([i**i for i in range(1, 1001)]) % 10**10


# hw 2:
def is_armstrong(number):
    return sum([int(s)**len(str(number)) for s in str(number)]) == number


# hw 3:
def collatz_steps(n):
    return 1 + collatz_steps(3*n + 1 if n % 2 else n // 2) if n > 1 else 0


# hw 4:
def make_cache(t):
    def decorator(func):
        cache = []

        def inner(*args, **kwargs):
            time_ = time.time()
            nonlocal cache
            while cache and cache[0][0] < time_:
                cache.pop(0)
            cached_return = [ret for _, args_, kwargs_, ret
                             in cache if args_ == args and kwargs_ == kwargs]
            cached_return = cached_return[0] if cached_return \
                else func(*args, **kwargs)

            cache.append((time.time() + t, args, kwargs, cached_return))
            return cache[-1][-1]
        return inner
    return decorator


@make_cache(30)
def slow_function(*args, **kwargs):
    time.sleep(60)
    return args, kwargs


if __name__ == '__main__':
    print(f'problem 6: {problem_6}') # problem 6: 25164150
    print(f'problem 9: {problem_9}') # problem 9: 31875000
    print(f'problem 40: {problem_40}') # problem 40: 210
    print(f'problem 48: {problem_48}') # problem 48: 9110846700

    assert is_armstrong(153) is True, 'Число Армстронга'
    assert is_armstrong(10) is False, 'Не число Армстронга'

    assert collatz_steps(16) == 4
    assert collatz_steps(12) == 9
    assert collatz_steps(1000000) == 152
