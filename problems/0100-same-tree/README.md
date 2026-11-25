# Same Tree

[LeetCode problem](https://leetcode.com/problems/same-tree/) · Journal date: 11/25 (year inferred as 2026 from the conversation).

## Original reasoning

The following is copied verbatim from the journal. It records the thinking at the time, including misconceptions.

```text
Same tree:
I’m thinking about a recursive approach. What should the function do? At each node, the function compares the two nodes, making sure than are the same, and then it will go to the left and then the right. return true if we reach the end. If two nodes are the same, then compare the leafs below. The core mechanism should work, but i need to be more specific about the conditions for true/false. If both nodes reach the end-> both are None, return true; if one node reach None, one is not, return false
```

## Original code

[Original code](original.py.txt) is preserved from the user’s conversation message, including any typos. It is stored as text to avoid implying it is ready to run. LeetCode supplies TreeNode and typing names.

## Review and complexity

O(n) worst-case time for matching trees and O(h) call stack. The original is already optimal. The and expression short-circuits after a mismatch.

## Revision status

No optimized replacement is needed. The original solution already expresses the recursive comparison correctly.
