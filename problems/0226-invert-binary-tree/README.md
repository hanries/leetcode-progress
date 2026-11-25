# Invert Binary Tree

[LeetCode problem](https://leetcode.com/problems/invert-binary-tree/) · Journal date: 11/24 (year inferred as 2026 from the conversation).

## Original reasoning

The following is copied verbatim from the journal. It records the thinking at the time, including misconceptions.

```text
11/24: invert binary tree
I’m not very familiar with this data structure, but i think the method is to depth first. i can only think of doing this with recursion. At each node, the base cases are if the node itself is none, -> return that node
if the node either leaf is none -> swap left and right. If both leaves have are valid, the left should be the same method done on the right one. Without recursion, we can use a stack, which is actually the data structure that recursion implicitly uses. Solved it
```

## Original code

[Original code](original.py.txt) is preserved from the user’s conversation message, including any typos. It is stored as text to avoid implying it is ready to run. LeetCode supplies TreeNode and typing names.

## Review and complexity

O(n) time and O(h) call stack. The original solution is already asymptotically optimal. The None base case handles missing children; separate leaf cases are unnecessary.

## Assisted revision

[Revised code](revised.py) is an assisted learning example, not an independently discovered solution. This is an iterative alternative, not a time-complexity improvement.
