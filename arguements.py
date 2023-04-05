def year_of_birth(name,age):
  year =2023-age
  print(f"hello {name},you were born in{year}")

def my_country(country="kenya"):
  print(f"you are from {country}")

def hello(*names):
  for name in names:
    print(f"hello{name}")

def sum(*nums):
  answer=0
  for num in nums:
    answer+=num
  return answer
  
def multiply_many(**kwargs):
  answer=1
  for num in kwargs.values():
    answer*=num
  return answer

# question1
  # A function named concatenate_args that takes any
#  number of string arguments in positional arguments format 
# and concatenates them into a single string
def concatenate_args(*args,text=" "):
    return text.join(args)
    
# question
# A function named concatenate_kwargs that takes any 
# number of string arguments in keyword arguments 
#  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    return ''.join(kwargs.values())
