# Group Anagrams

[LeetCode problem](https://leetcode.com/problems/group-anagrams/) · Journal date: 11/15, 11/16 (year inferred as 2026 from the conversation).

## Original reasoning

Copied verbatim from the journal, including mistakes and later discoveries.

### 11/15

```text
group anagrams: 11/15
I think to start, this problem obviously requires using dictionaries, because we want to find anagrams. if a string has the same dictionary of characters then it’s an anagram. But making a separate dictionary for each string seems overkill.
The algorithm: loop through the input, for each str, make a dictionary, then compare it to the rest of the array, group and remove if find anything, if not, proceed to the next str. do it until the input is empty.
This algorithm worked but it exceeded time limit: So far the worst time complexity is O(n^2).  it’s clear that the correct answer does not use nested loop. I thought i figured this out: first loop just creating a dictionary with the strs as the key, and their char dict as value. then loop through value to find the final answer. This one is hard, because looping through the value doesn’t give us the strings and it also requires nested loop. we can’t make the dictionaries themselves as values because they aren’t hashable. Is there any other way
Oh the key is to use tuple() that converts the dictionary into a hashable object
also list(dict.values()) automatically wraps the values into a list
```

### 11/16

```text
11/16:
want to go over group anagram again, revisiting the tuple method. Don’t forget to include .items(), because the count is how we distinguish each character
Then i want to think about how to implement it with an array of 26 characters. This could save space complexity to O(1). Use ord(), which returns the unicode value of a character. But a list is not hashable either, so tuple() is still needed
Another method to create keys is to use :
"".join(sorted(…)), which is the standard way to create sorted characters. Sorted() returns an array, and join() turns it into string again
```

## Code status

Notes only. Original code was not included in the supplied notes or recovered conversation. No reconstructed solution is presented as the original.

[Later technical corrections](../../journal/review-notes.md) are separate from the original reasoning.
