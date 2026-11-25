# Search a 2D Matrix

[LeetCode problem](https://leetcode.com/problems/search-a-2d-matrix/) · Journal date: 11/19 (year inferred as 2026 from the conversation).

## Original reasoning

Copied verbatim from the journal, including mistakes and later discoveries.

```text
11/19: search a 2d matrix
I think this problem is pretty intuitive, apply binary search to both rows and columns. I’m thinking do a binary search on the first number of each row first, to determine the row. The caveat is that for the rows, the number doesn’t have to match an exact row. Solved it, but had to add in another if statement to include the cases where it’s on the same row as mid_row. 
Simpler approach, this is very smart, since the matrix is sorted, we can convert it into a 1D array, by using the normal binary search algorithm from 0 to MxN -1
```

## Code status

Notes only. Original code was not included in the supplied notes or recovered conversation. No reconstructed solution is presented as the original.

[Later technical corrections](../../journal/review-notes.md) are separate from the original reasoning.
