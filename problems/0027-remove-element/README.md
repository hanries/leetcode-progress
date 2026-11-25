# Remove Element

[LeetCode problem](https://leetcode.com/problems/remove-element/) · Journal date: 11/14 (year inferred as 2026 from the conversation).

## Original reasoning

Copied verbatim from the journal, including mistakes and later discoveries.

```text
Remove Element: 11/14
this is similar to the problem that finds all the zero’s in an array and move to the back. The way i did that was to use two pointers, scan and write, scan finds the next non-zero, write is always on zero so it marks where to swap. My first answer is correct and use the right approach, but code could be written better. 
This problem doesn’t require us to keep the remaining elements the same as val so our algorithm could be simplified to simply finding non-val values and move them to the front. And only looping through the array once with no swap guarantees there wouldn’t be double counting.
```

## Code status

Notes only. Original code was not included in the supplied notes or recovered conversation. No reconstructed solution is presented as the original.

[Later technical corrections](../../journal/review-notes.md) are separate from the original reasoning.
