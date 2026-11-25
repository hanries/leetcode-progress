# Reverse Linked List

[LeetCode problem](https://leetcode.com/problems/reverse-linked-list/) · Journal date: 11/20 (year inferred as 2026 from the conversation).

## Original reasoning

Copied verbatim from the journal, including mistakes and later discoveries.

```text
11/20: reverse linked list
what makes this hard is that each node only stores its val and the next value. Intuitively, i can traverse to the end of the list first. Had to use gemini to fix my while loop condition, while temp is not None, instead of temp.next, i still don’t get it though. And I still need to figure out how to assemble a Linked list together, because having one variable doesn’t move with the list. So I think the idea is to have a dummy head, where dummy next is the beginning of the new linked list, and the ans moves through the arr. This is a lot harder than i expected, since i am pretty unfamiliar with this datastructure. Ended up creating dummy, which points to ans, and points to temp. So got it done with 3 variables.
But the optimal approach is to reverse it in place, using prev to keep track of the prev one, curr for current one, next, for next one. the key understanding is that only REFERENCE is changed when moving pointers, the object is the same
```

## Code status

Notes only. Original code was not included in the supplied notes or recovered conversation. No reconstructed solution is presented as the original.

[Later technical corrections](../../journal/review-notes.md) are separate from the original reasoning.
