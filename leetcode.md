# Review List
## [975](https://leetcode.com/problems/odd-even-jump/)
### Problem:
The core problem is: given an array of integers, for each number, find the smallest number on the right which is larger than it. Use the nearest if there is a tie.
### Solution:
If there is no **smallest** requirement, it is a monotonic stack problem. (Find the nearest one larger than the current one.)
We can treat each element as a tuple of (index, value).
We sort these tuples by value first, then index if tie. We got a new array.
Now the problem becomes find the nearest element on the right whose index is larger than the current on the new array.
It is solvable with monotonic stack.
As long as it is the nearest, we have ensured it is the smallest larger one and the nearest in the original array.

Monotonic stack: Find the nearest one on the right, which is larger than the current one.
The farther ones in the stack should be larger, the nearer ones should be smaller.
So every element in the stack should either be large or be near. At least have one merit.

## [686](https://leetcode.com/problems/repeated-string-match/)
### Problem:
Given two strings, A and B.
How many times we need to repeat A, so that B is a substring of A.
### Solution:
Repeat A until the string is as long as 2\*len(B) - 1, which is the maximum length needed to find the answer.
Use Rabin-Karp to hash the first len(B) chars in A, and sliding window one char by one char to the right.
Compare each of the hash value of the substrings to the hash value of B.
If not equal, then the substring is not B.
If equal, we check char by char to see if the substring is B or not.

[calculate inverse element](https://www.cnblogs.com/rainydays/p/4706219.html)

[Rabin-Karp](https://www.cnblogs.com/rainydays/archive/2011/06/23/2088081.html)
