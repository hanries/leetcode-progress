# Binary Search

[LeetCode problem](https://leetcode.com/problems/binary-search/) · Journal date: 11/13 (year inferred as 2026 from the conversation).

## Original reasoning

Copied verbatim from the journal, including mistakes and later discoveries.

```text
Binary Search: 11/13
pretty intuitive, find midpoint and recurse
what i learned: need to write the base cases for a recursive function first; tuple is an immutable type, and it’s hashable, a list is not hashable 
when calling recursion, pass in self. keyword.
problem with directly using mid point is thet we can’t return the exact index value, so pivot to the approach of creating another method. 
Nevermind, this is a lot harder than i expected, i’m still not very familiar with the implementation of recursion. 
Solved it, but the code is very ugly.
Cleaner version after consulting chat, first we can do it without recursion, second, the recursion could be improved, if we don’t include the mid in recursive steps, we can simplify the base case to just left>right
self. is only necessary for calling another function within the same class
```

## Code status

Notes only. Original code was not included in the supplied notes or recovered conversation. No reconstructed solution is presented as the original.

[Later technical corrections](../../journal/review-notes.md) are separate from the original reasoning.
