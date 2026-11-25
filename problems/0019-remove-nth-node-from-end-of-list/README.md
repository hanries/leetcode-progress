# Remove Nth Node From End of List

[LeetCode problem](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) · Journal date: 11/23 (year inferred as 2026 from the conversation).

## Original reasoning

Copied verbatim from the journal, including mistakes and later discoveries.

```text
11/23: remove nth list from end of the list
I think we should use two pointers, n nodes apart, the end pointer would start moving first, then the ans pointer starts moving after n-2 nodes has passed, and when end reaches the end, the ans node would skip the next node and continue the rest. If we let ans start at the dummy node, end start at head, then the gap is already 1, which is n = 2. Like usual, the edge cases when ans == none. Solved it, the hardest part was to count the correct number of offsets
```

## Code status

Notes only. Original code was not included in the supplied notes or recovered conversation. No reconstructed solution is presented as the original.

[Later technical corrections](../../journal/review-notes.md) are separate from the original reasoning.
