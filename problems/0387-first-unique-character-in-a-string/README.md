# First Unique Character in a String

[LeetCode problem](https://leetcode.com/problems/first-unique-character-in-a-string/) · Journal date: 11/10 (year inferred as 2026 from the conversation).

## Original reasoning

Copied verbatim from the journal, including mistakes and later discoveries.

```text
First Unique Character in a String: 11/10
thought process: we need to store two information for each character: the number of appearance, and it’s first index. and we have to loop through the whole string to do that.  
The problem i encountered is to find the characters with only one appearance and handle the edge case when there isn’t any character with only one appearance. I figured this out by storing both in a list as the value of the dictionary. 
To make my code more readable: use the enumerate(), which automatically keep track of the index and the character of an iterable object
```

## Code status

Notes only. Original code was not included in the supplied notes or recovered conversation. No reconstructed solution is presented as the original.

[Later technical corrections](../../journal/review-notes.md) are separate from the original reasoning.
