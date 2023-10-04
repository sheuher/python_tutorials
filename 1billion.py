#write a program that counts to 1,000,000,000 in python
from functools import cache, lru_cache
from numba import njit
import time

tic = (time.perf_counter())

"""@lru_cache(maxsize=400)
def counts():
    n=0
    while(n<1000000000): 
        n+=1
    return n

counts()"""

"""@cache
def counter(n):
    m = 0
    for i in range(n):
        m = i
    return m
    
print(counter(1000000000))
"""

@njit                   # alot faster ><, when using library njit doesn't know about, maybe doesn't work when adding function from libray into function
def counter(n):         # if low executions: time might be slower without njit
    m = 0               # first time slower: compiled needed, second time will be alot faster
    for i in range(n):  # with numba: paralization is also possible
        m = i
    return m
print(counter(1000000001))

"""#@njit                   # alot faster ><, when using library njit doesn't know about, maybe doesn't work when adding function from libray into function
def counter(n):         # if low executions: time might be slower without njit
    m = 0
    for i in range(n):
        m = i
    return m
print(counter(100))"""

"""from mypyc.build import mypycify # doesn't really work mypyc
from setuptools import setup

setup(
    name='lcs',
    packages=['lcs'],
    ext_modules=mypycify(['lcs/mypyc_.py']),
)

def counter(n:int):         
    m = 0                
    for i in range(n):  
        m = i
    return m
print(counter(1000000000))"""

toc = (time.perf_counter())

print(toc-tic)

# conclusion
# while loop < for loop < sum range (build in) < numpy sum <  math sum