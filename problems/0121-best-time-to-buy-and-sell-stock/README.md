# Best Time to Buy and Sell Stock

[LeetCode problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · Journal date: 11/12 (year inferred as 2026 from the conversation).

## Original reasoning

Copied verbatim from the journal, including mistakes and later discoveries.

```text
Best time to buy and sell stocks: 11/12
my thought is to use two pointers, cuz we are trying to find the biggest gap between left and right, and use a max variable to keep track of the current max profit. Loop from index 0 forward, if the next price is bigger than the current price, hold buy and move the sell to the next price; when the next price is equal or smaller than the current price, move the buy to the current price and move the sell to the next.
Really isn’t too hard, just gotta figure out the right logic.
```

## Code status

Notes only. Original code was not included in the supplied notes or recovered conversation. No reconstructed solution is presented as the original.

[Later technical corrections](../../journal/review-notes.md) are separate from the original reasoning.
