from functools import wraps
from datetime import datetime
from time import perf_counter


def odd_it(fn: "Function"):
	'''Decorator that allows to run a function only at odd seconds, 
	else prints out "We're even!"'''
	current_time = 0
	def inner(*args, **kwargs):
		'''innef function of the decorator'''
		nonlocal current_time
		current_time = datetime.now().second
		print(f'current instance of second is {current_time}')
		if current_time%2 !=0:
			return fn(*args, **kwargs)
		else:
			return None
		
	return inner



def logger(fn: "Function"):
	''' looger function which will will be tested against a 
	function that will be sent 2 parameters, and it would return some random string. '''
	from functools import wraps
	from datetime import datetime, timezone
	from time import perf_counter


	@wraps(fn)
	def inner(*args, **kwargs):
		'''innef function of the decorator'''
		run_dt = datetime.now(timezone.utc)
		start = perf_counter()
		result = fn(*args, **kwargs)
		end = perf_counter()
		print(f'{fn.__name__}: called at {run_dt} and Execution time: {end-start}')
		print(f'Function description:{fn.__doc__}')
		print(f'Function annotation:{fn.__annotations__}')
		return result
		
		
		

	return inner

	


def decorator_factory(access:str):
	'''start with a decorator_factory that takes an argument one of these strings
	 high, mid, low or no then write the decorator that has 4 free variables based on the 
	 argument set by the factory call, give access to 4, 3, 2 or 1 arguments to the function 
	 being decorated from var1, var2, var3, var4'''

	def decor(fn):
		'''Decorator to check the access level and provide variable access'''
		a=6
		b=4
		c=3
		d=8

		def inner(*args, **kwargs):
			'''inner function of the decorator'''
			
			nonlocal a,b,c,d

			if access == 'high':
				return a,b,c,d
			elif access == 'mid':
				return a,b,c
			elif access == 'low':
				return a,b
			elif access == 'no':
				return a, 
			else:
				return'Improper access keyword set'
		return inner
	return decor


	


def authenticate(set_password):
	'''decorator factory to authenticate a user to acces the function'''
	def auth_area(fn):
		''' decorator to checck the access'''
		def inner(*args, **kwargs):
			'''inner function of the decorator'''
			if len(args)>0:
				
				if args[0]=='secret':
					return fn()
				else:
					return "Wrong Password"
			else:
				if set_password=='secret':
					return fn()
				else:
					return "Wrong Password"
		return inner
	return auth_area



def timed(num_reps):
	'''decorator factory to run a function 'n' number of times and return the average time to run the function'''
	def timed_dec(fn):
		'''Decortor to time a function'''
		from time import perf_counter
		def inner(*args, **kwargs):
			'''inner function of the decorator'''
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
	return timed_dec
	


