# Climbing Stairs

[LeetCode problem](https://leetcode.com/problems/climbing-stairs/) · Journal date: 11/14 (year inferred as 2026 from the conversation).

## Original reasoning

Copied verbatim from the journal, including mistakes and later discoveries.

```text
Climbing stairs: 11/14
I have done something similar to this before, and i have solved this problem previously. So the method i think is to use dynamic programming. gradually build up the steps. For example, when n= 3, the previous step could either be n = 1 or n = 2. There is only one way to be n = 1 and 2 ways to be n = 2, so there are 1 + 2 = 3 ways to get to 3. The hardest part is to understand the logic clearly. For n =4, we can go from n= 3 or n =2, so there would be 3+2 ‎ = 5ways to go to 4. Not too hard, but remember to handle the edge case when n=1. Use pointers could save some space
```

## Code status

Notes only. Original code was not included in the supplied notes or recovered conversation. No reconstructed solution is presented as the original.

[Later technical corrections](../../journal/review-notes.md) are separate from the original reasoning.
