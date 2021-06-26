
# 1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable

def counter(fn):
     '''closure to check whethet the function has docstring or not'''
     docstringlen = 50
     def inner(*args, **kwargs):
          nonlocal docstringlen
          #docstringlen = 80

          

          if fn.__doc__ == None:
               print(f'Function {fn.__name__}()has no Docstring Present')

          else:
               l  =  len(fn.__doc__)

               if l >= docstringlen :
                    print(f'Function {fn.__name__}() has docstring length {l}, more than {docstringlen} Character')
               else:
                    print(f'Function {fn.__name__}() has docstring length {l}, less than {docstringlen} Character')

          return fn(*args, **kwargs)

     return inner

def add(a,b):
     """ this is add function which job is to add  two numbers"""
     
     return a+b

c_add = counter(add)
c_add(2,3)




#2. Write a closure that gives you the next Fibonacci number

def Fibonacci():
     """Closure to find next  fibonacci """

     fib_list  = [0,1]


     def fib_finder(n):
          nonlocal fib_list

          if n<= 0:
               return "Incorrect Output"
          
          if n > 2:
               for i in range (2, n):
                    fib_list.append(fib_list[i-1] + fib_list[i-2])
          return fib_list[n-1]

     return fib_finder

f = Fibonacci()
n = f(9)
print(n)




#3. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts

def mult(a, b):
    '''this is mul function which job is to multiply  two numbers'''
    return a * b


def add(a, b):
    '''this is add function which job is to add  two numbers'''
    return a + b

def div(D,d):
     '''this is div function which job is to divide one number by othe two number'''
     return D/d

counters = dict()

def counter(fn):
    '''Closure to keep  count the number  of times a function called'''
    cnt = 0  # initially fn has been run zero times
    
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt  # counters is global
        return fn(*args, **kwargs)
    
    return inner


counted_add = counter(add)
counted_mult = counter(mult)
counter_div =  counter(div)

counted_add(1, 2)
counted_add(1, 2)
counted_add(1, 2)
counted_add(1, 2)
counted_add(1, 2)
counted_mult(1, 2)
counted_mult(1, 2)
counted_mult(1, 2)
counter_div(5,2)

print(counters)




#4. Modify above such that now we can pass in different dictionary variables to update different dictionaries

def mult(a, b):

    '''this is mul function which job is to multiply  two numbers'''
    return a * b


def add(a, b):
    '''this is add function which job is to add  two numbers'''
    return a + b

def div(D,d):
    '''this is div function which job is to divide one number by othe two number'''
    return D/d

counters = dict()

def counter(fn):
    '''Closure to keep  count the number  of times a function called'''
    cnt = 0  # initially fn has been run zero times
    
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1

        if fn.__name__ =='add':
            counters['add'] = cnt
        if fn.__name__ =='mult':
            counters['mult'] = cnt
        if fn.__name__ =='div':
            counters['div'] = cnt

        #counters[fn.__name__] = cnt  # counters is global
        return fn(*args, **kwargs)
    
    return inner

c = counter(add)
c(1,2)
c(1,2)
c = counter(mult)
c(3,4)
c(4,5)
c = counter(div)
c(6,2)
c(8,2)


print(counters)
















