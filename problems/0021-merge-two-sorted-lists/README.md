# Merge Two Sorted Lists

[LeetCode problem](https://leetcode.com/problems/merge-two-sorted-lists/) · Journal date: 11/21 (year inferred as 2026 from the conversation).

## Original reasoning

Copied verbatim from the journal, including mistakes and later discoveries.

```text
11/21: Merge Two Sorted Linked Lists 
natural follow up from the previous question. Intuitively we need three pointers, one for each list and then a dummy that just points to the beginning of the answer. Problem 1: what does dummy.next point to? Should be the beginning of the answer, so list1? but list1 itself doesn’t get changed. We need to create a new ListNode for every new ans.
Actually i don’t need to create a new linked list. I just need to make sure a dummy always points at the beginning of the answer. ans and top can move around freely. A key misunderstanding i have was i thought top = top.next would be fine, since top was initiailized on the “top” list, but each node only stores its own value and the next reference, it doesn’t care where it sits at. 
Misunderstanding 2: at the beginning, ans should be = dummy, since ans is a pointer, and dummy.next should always be the beginning of the answer.
variables are like labels. they point at objects, but a single object could be reachable from different labels.
```

## Code status

Notes only. Original code was not included in the supplied notes or recovered conversation. No reconstructed solution is presented as the original.

[Later technical corrections](../../journal/review-notes.md) are separate from the original reasoning.
