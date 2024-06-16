# Python Grammar

## Common Mistakes
* When use '', "", (), [], and {}, type the pair before insert the contents.
* () and [] can be easily misused with each other.
* `for index, elem in enumerate(...):`. index before elem.
* Use `//` to divide integers and get integer part of the result.
## Data Structures
### Queue & Stack
```python
import collections
dq = collections.deque()
dq.append(1)
dq.append(2)
dq.appendleft(3)
print(dq)  # [3, 1, 2]
dq.pop()
print(dq)  # [3, 1]
dq.popleft()
print(dq)  # [1]
while dq:
  a = dq.popleft()
  ...
print(dq[-1])
```
### Hash Table
```python
a = {}
a['ab'] = 5
print('ab' in a)  # True
print(a['ab'])  # 5
a.pop('ab')
print('ab' in a)  # False

a = collections.defaultdict(lambda : 0)
a = collections.defaultdict(list)

# Set is not subscriptable.
a = set()
a.add('ab')
print('ab' in a)  # True
a.remove('ab')
print('ab' in a)  # False
```
### Heap
```python
import heapq
hp = heapq.heapify([1, 5, 8, 2, 3])
heapq.heappush(hp, 9)
print(heapq.heappop(hp))  # 1
# Use negative value if want a max heap.
# or use cmp_to_key(cmp).
```
### Comparison
```python
# Traditional cpp style cmp function.
def cmp(a, b):
    return a - b

from functools import cmp_to_key

list_b = sorted(list_a, key=cmp_to_key(cmp))

# For anything not supporting key argument
# wrap them into a class with cmp as comparison function
k_class = cmp_to_key(cmp)
list_b = []
for a in list_a:
  list_b.append(k_class(a))
list_b = sorted(list_b)
for b in list_b:
  print(b.obj)
```
## Iterator

### Product
```python
from itertools import product
product('ABCD', 'xy') # list of tuples, Ax Ay Bx By Cx Cy Dx Dy
```
### Group By
```python
from itertools import groupby
[k for k, g in groupby('AAAABBBCCDAABBB')]  # --> ['A', 'B', 'C', 'D', 'A', 'B']
[list(g) for k, g in groupby('AAAABBBCCD')]  # --> [['A','A','A','A'], ['B','B','B'], ['C','C'], ['D']]
```
### Combination
```python
from itertools import combinations, combinations_with_replacement
combinations('ABCD', 2)  # list of tuples AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2)  # list of tuples AA AB AC AD BB BC BD CC CD DD
```
### Permutation
```python
from itertools import permutations
permutations('ABCD', 2)  # list of tuples AB AC AD BA BC BD CA CB CD DA DB DC
```
## Strings
### Split Strings
```python
a = 'aba'
print(a.split('a'))  # ['', 'b', '']
print(a.split('x'))  # ['aba']
```
### Count Occurance
```python
a = 'abababa'
print(a.count('aba'))  # 2
```
### Case Changes
```python
a = 'aBA'
print(a.upper())  # ABA
print(a.lower())  # aba 
```
### Check single char

```python
a.isdecimal()  # True if a consists of 0-9
a.islower()  # True if a consists of a-z
a.isupper()  # True if a consists of A-Z
a.isalpha()  # True if a consists of a-z,A-Z.
```

## I/O
### From File
```python
file = open('somefile')
for line in file:
  do_something()
file.close()
```
### From standard IO
```python
import sys

for line in sys.stdin:
  do_something()
```
