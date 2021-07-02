# Session-08
---
## Decorators

Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it. But before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.

decorator function added some new functionality to the original function. This is similar to packing a gift. The decorator acts as a wrapper. The nature of the object that got decorated (actual gift inside) does not alter. But now, it looks pretty (since it got decorated).

[source of the above content
](https://www.geeksforgeeks.org/decorators-in-python/)

## Decorator Factory
You would use a decorator factory if you want your decorator's behavior to be controlled dynamically via parameters (just like with any regular function). 

A decorator factory is just a callable that produces the actual decorator. It is used to make it possible to 'configure' a decorator.

[Link](https://stackoverflow.com/questions/28693930/when-to-use-decorator-and-decorator-factory)

## Note:
There is a bit of confusion indeed with decorators in python.

This is due to the fact that a decorator with arguments is not actually a decorator but a decorator factory, as noted by others. So to implement a decorator that can be called without and with arguments, it is a bit tricky.

people tend to think that decorators are necessarily function wrappers, like in your example. But that's not the case: a decorator can entirely replace the decorated function or class by something else (not even a function or class!).

    


## Assignment 

### 1. Write a decorator that allows a function to run only on odd seconds
```python

from datetime import datetime

def odd_it(fn: "Function"):
    current_time = 0
    def inner(*args, **kwargs):
        nonlocal current_time
        current_time = datetime.now().second
        print(f'current instance of second is {current_time}')
        if current_time%2 !=0:
            return fn(*args, **kwargs)
        else:
            return "We're even!"
        
    return inner


@odd_it
def add(a,b):
    return a+b


d = add(3,5)
print(f'{d}')
```

### 2. Write a decorator to log a function
```python
import random
import string

def logger(fn: "Function"):
    from functools import wraps
    from datetime import datetime, timezone
    

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f'{fn.__name__}: called {run_dt}')
        return result

    return inner

@logger
def randomfun(a,b):

    length = 8
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


print(randomfun(3,4))
```
### 3. Write a decorator to authenticate a user to acces the function

```python
def authenticate(set_password):
    def auth_area(fn):
        def inner():
            if set_password=='secret':
                return fn()
            else:
                return "Wrong Password"
        return inner
    return auth_area


@authenticate("secrets")
def my_func():
    return "Amazing!"



print(my_func())
```

### 4. Write a decorator to run a function 'n' number of times and return the average time to run the function
```python
def timed_factory(num_reps):
    def timed(fn):
        from time import perf_counter
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_elapsed = total_elapsed / num_reps
            print(f'Avg Run time for {num_reps} times: {avg_elapsed}')
            return result
        return inner
    return timed

@timed_factory(5)
def exp(n,m):
    return n**m

print(exp(3,4))

```

### 5. Write a decorator which provides privilege access to a class that has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params)

```python
def dec_factory(level):
    def decor(fn):
        a=6
        b=4
        c=3
        d=8

        def inner(*args, **kwargs):
            
            nonlocal a,b,c,d

            if level == 'high':
                return a,b,c,d
            elif level == 'mid':
                return a,b,c
            elif level == 'low':
                return a,b
            elif level == 'no':
                return a, 
            else:
                return'Improper access keyword set'
        return inner
    return decor


def func(*args):
    return args

l = len(dec_factory('')(func)())
print(l)
```