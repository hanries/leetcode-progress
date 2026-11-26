# My LeetCode journal

I'm practicing LeetCode in Python and writing down how I think through each problem. I usually start with whatever approach makes sense to me, try to get it working, then look at what I could do better. Some problems take much longer than I expect.

The part I keep getting stuck on is turning an idea into code. With Diameter of Binary Tree, I figured the helper should calculate both height and diameter, but I didn't know how to return both. Learning that Python could return a tuple cleared up something I'd spent hours trying to work around.

I want to be able to come back to these notes and see what I was thinking, including the approaches I abandoned too early. I also want to redo problems without looking at my old solutions and see whether I understand them better.

## What's here

My [original journal](journal/original-notes.txt) covers November 6 to 25. I've kept the wording as I wrote it, so some entries have typos or explanations I later realized were wrong. Those corrections are in [separate review notes](journal/review-notes.md).

Each problem has its own page with my thought process. I've included my original code where I still have it. Most of the earlier entries are notes only; I haven't filled in missing code with a new solution and called it my original attempt.

I used ChatGPT and, for some problems, Gemini when I got stuck. I keep the solutions I learned with help separate from my own attempts. The assisted revisions include explanations and complexity analysis so I can work through why they work.

## Problems I've worked on

There are 31 problems here, with a second entry for Group Anagrams when I revisited it. Dates follow my original notes; the year is treated as 2026 based on the conversation where I shared them.

| Problem | Journal date | Contents |
|---|---|---|
| [1. Two Sum](problems/0001-two-sum/) | 11/6 | Original notes |
| [242. Valid Anagram](problems/0242-valid-anagram/) | 11/8 | Original notes |
| [1480. Running Sum of 1d Array](problems/1480-running-sum-of-1d-array/) | 11/9 | Original notes |
| [1920. Build Array from Permutation](problems/1920-build-array-from-permutation/) | 11/10 | Original notes |
| [1672. Richest Customer Wealth](problems/1672-richest-customer-wealth/) | 11/10 | Original notes |
| [217. Contains Duplicate](problems/0217-contains-duplicate/) | 11/10 | Original notes |
| [387. First Unique Character in a String](problems/0387-first-unique-character-in-a-string/) | 11/10 | Original notes |
| [283. Move Zeroes](problems/0283-move-zeroes/) | 11/11 | Original notes |
| [121. Best Time to Buy and Sell Stock](problems/0121-best-time-to-buy-and-sell-stock/) | 11/12 | Original notes |
| [20. Valid Parentheses](problems/0020-valid-parentheses/) | 11/12 | Original notes |
| [704. Binary Search](problems/0704-binary-search/) | 11/13 | Original notes |
| [70. Climbing Stairs](problems/0070-climbing-stairs/) | 11/14 | Original notes |
| [27. Remove Element](problems/0027-remove-element/) | 11/14 | Original notes |
| [26. Remove Duplicates from Sorted Array](problems/0026-remove-duplicates-from-sorted-array/) | 11/15 | Original notes |
| [49. Group Anagrams](problems/0049-group-anagrams/) | 11/15, 11/16 | Original notes |
| [167. Two Sum II Input Array Is Sorted](problems/0167-two-sum-ii-input-array-is-sorted/) | 11/16 | Original notes |
| [155. Min Stack](problems/0155-min-stack/) | 11/17 | Original notes |
| [35. Search Insert Position](problems/0035-search-insert-position/) | 11/18 | Original notes |
| [3. Longest Substring Without Repeating Characters](problems/0003-longest-substring-without-repeating-characters/) | 11/18 | Original notes |
| [74. Search a 2D Matrix](problems/0074-search-a-2d-matrix/) | 11/19 | Original notes |
| [206. Reverse Linked List](problems/0206-reverse-linked-list/) | 11/20 | Original notes |
| [21. Merge Two Sorted Lists](problems/0021-merge-two-sorted-lists/) | 11/21 | Original notes |
| [876. Middle of the Linked List](problems/0876-middle-of-the-linked-list/) | 11/22 | Original notes |
| [141. Linked List Cycle](problems/0141-linked-list-cycle/) | 11/22 | Original notes |
| [203. Remove Linked List Elements](problems/0203-remove-linked-list-elements/) | 11/22 | Original notes |
| [19. Remove Nth Node From End of List](problems/0019-remove-nth-node-from-end-of-list/) | 11/23 | Original notes |
| [226. Invert Binary Tree](problems/0226-invert-binary-tree/) | 11/24 | Original notes and code; assisted revision |
| [110. Balanced Binary Tree](problems/0110-balanced-binary-tree/) | 11/24 | Original notes and code; assisted revision |
| [104. Maximum Depth of Binary Tree](problems/0104-maximum-depth-of-binary-tree/) | 11/25 | Original notes |
| [100. Same Tree](problems/0100-same-tree/) | 11/25 | Original notes and code |
| [543. Diameter of Binary Tree](problems/0543-diameter-of-binary-tree/) | 11/25 | Original notes and code; assisted revision |

## How I keep track of attempts

- `original.py.txt` is my original code, including any typos. I keep it as text so an unfinished attempt doesn't look like a ready-to-run solution.
- `intermediate.py.txt` is a later attempt I made while working through the same problem.
- `revised.py` is a solution or alternative I learned with help.
- The review sections explain what I learned afterward, separately from what I was thinking at the time.

I record submission results when I have them. Passing local checks doesn't mean a solution was accepted on LeetCode.

I'll use this [entry template](ENTRY_TEMPLATE.md) for future problems and revisits.
