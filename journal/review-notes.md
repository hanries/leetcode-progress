# Review of earlier journal notes

These later corrections leave the original journal unchanged.

- Python lists grow dynamically. Assignment to a nonexistent index fails; append adds a new element. Preallocating is one option.
- A tuple is hashable only when all of its elements are hashable.
- For Group Anagrams, a character-count key must be canonical: use a fixed 26-count tuple for lowercase English letters or sorted character-count pairs. Merely converting dictionary items to a tuple can preserve different insertion orders and produce different keys for anagrams.
- The 26-count working array is constant size for a fixed alphabet. The complete grouping algorithm still stores groups and keys; it is not O(1) total space.
- Min Stack can provide O(1) time per operation while using O(n) total storage. Storing a value and its current minimum together does not make total space constant.
- Best Time to Buy and Sell Stock should track the smallest price seen so far. Resetting the buy point after every local decline can miss the best trade.
- self is the instance parameter by convention; use self.method() for instance method access. A standalone or nested helper does not need self.
- Flattened matrix binary search can use index // columns and index % columns without constructing a new array.
- For diameter, the tuple base case must be (0, 0), and each child helper should be called once. Repeatedly calling the helper to extract separate tuple components defeats the optimization.
