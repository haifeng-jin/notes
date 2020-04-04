# Review List
## [975](https://leetcode.com/problems/odd-even-jump/)
### Problem
The core problem is: given an array of integers, for each number, find the smallest number on the right which is larger than it. Use the nearest if there is a tie.
### Solution
If there is no **smallest** requirement, it is a monotonic stack problem. (Find the nearest one larger than the current one.)
We can treat each element as a tuple of (index, value).
We sort these tuples by value first, then index if tie. We got a new array.
Now the problem becomes find the nearest element on the right whose index is larger than the current on the new array.
It is solvable with monotonic stack.
As long as it is the nearest, we have ensured it is the smallest larger one and the nearest in the original array.

### Algorithms
#### Monotonic stack
Find the nearest one on the right, which is larger than the current one.
The farther ones in the stack should be larger, the nearer ones should be smaller.
So every element in the stack should either be large or be near. At least have one merit.

## [686](https://leetcode.com/problems/repeated-string-match/)
### Problem
Given two strings, A and B.
How many times we need to repeat A, so that B is a substring of A.
### Solution
Repeat A until the string is as long as 2\*len(B) - 1, which is the maximum length needed to find the answer.
Use Rabin-Karp to hash the first len(B) chars in A, and sliding window one char by one char to the right.
Compare each of the hash value of the substrings to the hash value of B.
If not equal, then the substring is not B.
If equal, we check char by char to see if the substring is B or not.

### Algorithms
#### [calculate inverse element](https://www.cnblogs.com/rainydays/p/4706219.html)
#### [Rabin-Karp](https://www.cnblogs.com/rainydays/archive/2011/06/23/2088081.html)

## [398](https://leetcode.com/problems/random-pick-index/)
### Problem
Given an array, go through it for once to find a target value and output the index.
If there are ties, pick each one with equal probability.
### Solution
Pure reservoir sampling problem.
### Algorithm
#### Reservoir sampling
Given an array of length unknown, only going through it for once and pick m out of it with equal probability.

We keep a set of size m.
As we go through the first m elements, we just add them to the set.

If we arrived at the ith (i > m) element, since we don't know the length, this one could be the last element in the array.
If it is the last, we have to pick it with a probability of m/i, which is the equal probability for each element.
Since we don't know, we just treat it as the last.

If it is not picked, we just move to the next one.
If it is picked, we replace one of the m elements in the set with equal probability.

We keep doing this until we get to the end of the array.
No matter where we stop, we always have the equal probability to pick each one.

Prove with mathematical induction:
If the m elements we picked after going through the first (i-1) elements is m/(i-1) each,
the probability of keeping one of these m elements in the set instead of being replaced by the new one is:
(1-m/i) + (m/i)\*(1/m) = m/i.
Since the condition is satisfied with i=m, so all the following should be satisfied.
Proved.

A variation of the problem would be, We can only pick the elements satisfying certain condition, for example, only picking prime numbers in an array of integers with equal probability.
We just change the definition of i from the number of elements we have gone through to the number of elements we have gone through and satisfiying the condition.
