# Review List
## [975. Odd Even Jump](https://leetcode.com/problems/odd-even-jump/)
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

## [398 Random Pick Index](https://leetcode.com/problems/random-pick-index/)
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

## [843. Guess the Word](https://leetcode.com/problems/guess-the-word/)
### Problem
Given 100 words of length 6, one of which is the target.
You pick one at a time to query how many matches in letters between the one you pick and the target.
Matches is calculated as: 

"abbccd" and 

"aabbcc" has 3 matches at index 0, 2, 4.
You need to pick the target within 10 queries.
### Solution
A simple solution would be after each query we filter the list of words.
For example, the query says the picked one and the target has x matches.
We check the matches of the picked one with all the words.
Only keep the ones having x matches with the picked word.
Next time, we just randomly pick one from the filtered list.

This solution won't pass.
A better solution would be not randomly pick.
We want the size of the filtered list to be small after a query.
Given a word, there are only 7 possible outcomes of the query (0~6 matches).
Each of the outcome would result in a different size of the filtered list.
We use the maximum among the 7 as the indicator of whether we should pick it.
We just compute the indicator of all the words in the list before we pick one with the smallest indicator.

The reason we use the maximum as the indicator is because we want to garantee the worst case since we only have 10 chances.

## [363. Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)

### Problem
Given a 2-d array, with integer values (positive and negative).
Given an integer k.
Find the maximum sub-matrix sum <= k.

### Solution
We can use dynamic programming to calculate the sums of the sub-matrices.
Then by enumerating all the sub-matrices, we can get the answer.
Complexity O(n^2m^2).
An improve would be only enumerate the top, bottom and right border of the sub-matrix.
Since we want 
For the left border we just select the left that maximize sum[right] - sum[left] subject to <= k,
where sum is the sum of the sub-matrix with left=0 to right=index and the current top and bottom border.
To maximize it, we can use binary search tree.
It is equivalent to maximizing sum[left] subject to >= sum[right] - k.
We insert the sum values into the tree, every time we query it the lower_bound of sum[right] - k, as we iterate all the right.
The complexity is O(n^2mlogm).

Note: Python doesn't have a built-in binary search tree. We need to write our own.
