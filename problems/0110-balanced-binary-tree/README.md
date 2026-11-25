# Balanced Binary Tree

[LeetCode problem](https://leetcode.com/problems/balanced-binary-tree/) · Journal date: 11/24 (year inferred as 2026 from the conversation).

## Original reasoning

The following is copied verbatim from the journal. It records the thinking at the time, including misconceptions.

```text
Balanced binary tree:
we need a step counter in the recursion, I’m thinking including in the arguments, but what should the recursive function return, boolean or the step count. This is taking a lot longer than I expected to figure out. What I want the algorithm to do: At each node, compare the depthL and depthR, is the difference is greater than 1, than return false. Now how should depthL and depthR be calculated? We can’t just do keep passing the same two variables, because they should be relative to the single parent node. So we +1 when the function returns. But what should the main function include? Another recursive function? Wouldn’t that be wasting resources. But we need to a way to convert the counts into a boolean output. I feel like i haven’t touched the root of the problem. What do want from each node? How deep is your left leaf and how deep is your right?
```

## Original code

[Original code](original.py.txt) is preserved from the user’s conversation message, including any typos. It is stored as text to avoid implying it is ready to run. LeetCode supplies TreeNode and typing names.

## Review and complexity

The original repeatedly calculates subtree heights. O(n²) is a valid upper bound; short-circuiting can stop this particular implementation early, so a skewed tree alone does not establish a quadratic worst case. The assisted revision visits each node at most once: O(n) time and O(h) stack. A -1 sentinel must be checked before height arithmetic.

## Assisted revision

[Revised code](revised.py) is an assisted learning example, not an independently discovered solution. It keeps child results so each subtree is computed only once.
