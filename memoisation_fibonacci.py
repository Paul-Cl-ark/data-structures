from time import time 
import sys

def fib_memo(n, memo = {}):
  if n <= 2: return 1
  if n not in memo: memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
  return memo[n]

def fib_tab(n):
  if n <= 2: return 1
  tab = [0, 1]
  
  for num in range(2, n + 1):
      tab.append(tab[num - 1] + tab[num -2])

  return tab[n]



# def slow_fib(n):
#   if n <= 2: return 1
#   return slow_fib(n - 1) + slow_fib(n - 2)

start = time()
print(fib_tab(1000))
print('TAB: ', time() - start)
start_1 = time()
print(fib_memo(999))
print('MEMO: ', time() - start_1)
# start_2 = time()
# print(slow_fib(40))
# print('slow: ', time() - start_2)
