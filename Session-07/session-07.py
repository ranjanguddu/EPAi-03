


#3. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts

def mult(a, b):


     '''this is mul function which job is to multiply  two numbers'''
     return a * b


def add(a, b):
     '''this is add function which job is to add  two numbers'''
     return a + b

def div(D,d):
     '''this is div function which job is to divide one number by other'''
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




















