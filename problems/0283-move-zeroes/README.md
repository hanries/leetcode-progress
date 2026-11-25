# Move Zeroes

[LeetCode problem](https://leetcode.com/problems/move-zeroes/) · Journal date: 11/11 (year inferred as 2026 from the conversation).

## Original reasoning

Copied verbatim from the journal, including mistakes and later discoveries.

```text
Move Zeroes 11/11
my thought is that loop through the list backwards, when see a zero, swap the zero with the number next to it, repeat the process;
if encountered another zero, couldn’t really figure it out. —> go two loops, main one goes backwards, so no 0’s gets missed, the smaller one go forward, to swap
one pitfall i fell for: safe index should be updated to the inner loop not the outer loop: safe = j
the two pointer method is smart, but the key thing is to realize thet moving all non-zero saves a pass
```

## Code status

Notes only. Original code was not included in the supplied notes or recovered conversation. No reconstructed solution is presented as the original.

[Later technical corrections](../../journal/review-notes.md) are separate from the original reasoning.
