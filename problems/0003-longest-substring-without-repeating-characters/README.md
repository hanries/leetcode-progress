# Longest Substring Without Repeating Characters

[LeetCode problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · Journal date: 11/18 (year inferred as 2026 from the conversation).

## Original reasoning

Copied verbatim from the journal, including mistakes and later discoveries.

```text
Longest Substring Without Repeating Characters:
this is a classic sliding window problem since we are trying to find the substring
The algorithm should have a left and a right pointer.
Every step we check if left and right are the same, if they are left adds one, if not right adds one. we calculate the current max by using right - left + 1 before moving left. We need to way to make sure there is no repetition within the interval. Hashset? Hashset works, Think about sliding window, we only need to care about what is in the window, and nothing else. By resetting the hashset everytime we move left, we can solve this. 
Intuitively time complexity could be improved. Right shouldn’t need to reset to left every time. -> we can just find the largest window size, and move the entire window to the right, the window itself should be a set.  This works, If we use ASCII, then we can further simplify, this solution O(2n) at worst. No nested loop
```

## Code status

Notes only. Original code was not included in the supplied notes or recovered conversation. No reconstructed solution is presented as the original.

[Later technical corrections](../../journal/review-notes.md) are separate from the original reasoning.
