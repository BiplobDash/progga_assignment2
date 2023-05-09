
import time
def execution_time_log(func):
   def wrapper():
      start_time = time.time()
      result = func()
      end_time = time.time()
      return result
   return wrapper

@execution_time_log
def long_running_func():
  for x in range(1000000):
      print(x)