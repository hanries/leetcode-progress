# Binary Tree Paths

[LeetCode problem](https://leetcode.com/problems/binary-tree-paths/) · November 26, 2026

## My original reasoning

```text
binary tree paths: Each child node adds one more path, recurse through left and right. The recursive function should return the node value itself and add it to the current path. Each function should answer the question what are the paths to the leaf from this node. Now what should each node return? It should return a list of paths from the current node to the leafs. To do this, we simply add the current node’s value to the existing string. The current method would always return a runtime error because it tries to iterate on none, so i added a conditional statement before looping through the list.  Now I need to pay more attention to the return format. the path list should always contain str(root.val), but it should only add to the existing paths if those paths exist. I finished it, but i feel like i can simplify the code a lot. 
```

## My original code

[Original attempt](original.py.txt). The pasted formatting has been normalized. My checks before the loops avoid iterating over None, and the code produces the paths for a nonempty tree. For an empty tree, it returns None even though the annotation says list[str]. I haven't recorded an accepted submission here.

## Bottom-up approach with assisted cleanup

[Cleaned-up code](revised.py)

Each call returns all paths from its node to a leaf. The parent adds its own value to the front of each path it gets back. That's the bottom-up part: the children return complete paths before the parent builds its paths.

The empty-tree case returns `[]`. A leaf returns `[str(root.val)]`. Every call now returns the same kind of result, so I can loop over a child's paths without checking whether that result is None. An empty list simply runs the loop zero times.

I handle leaves explicitly before combining child paths. Then I use the same loop for both children instead of writing the string-building code twice. This keeps my original recursive idea; it's a cleanup rather than a new algorithm.

Python strings are immutable, so adding a prefix copies the string. This approach can take O(n²) time on a chain even though it visits each node once, assuming bounded-width node values. It uses O(h) recursive stack space, plus storage for path strings. A path-buffer traversal is an alternative if I want to avoid repeatedly copying each path at every ancestor.
