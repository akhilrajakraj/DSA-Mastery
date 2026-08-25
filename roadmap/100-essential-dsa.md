# 100 Essential DSA Problems — Mastery Roadmap

> **Purpose:** Build DSA pattern recognition through deliberate practice.
>
> This roadmap is based on the supplied **100 Essential LeetCode & DSA Problems** PDF. The source organizes the 100 problems into 34 Easy, 40 Medium, and 26 Hard problems and labels the primary pattern for each problem. fileciteturn80file0L2-L8 fileciteturn80file0L42-L49 fileciteturn80file0L85-L91

## How We Will Use This Roadmap

We will **not** memorize 100 solutions.

For every problem, the goal is to recognize:

1. What is the problem asking?
2. What information must be maintained?
3. What pattern does the problem suggest?
4. What is the smallest useful clue?
5. Can I design the algorithm before writing code?
6. Can I explain the time and space complexity?
7. Can I implement it without looking at a solution?
8. Can I solve a small variation after the original problem?

### Mastery rule

A problem is not considered mastered just because the code passes once.

For each problem we will aim for:

```text
Understand → Recognize → Explain → Design → Implement → Test → Document → Reattempt
```

---

# Phase 1 — Easy Problems

The source lists problems 1–34 as Easy. fileciteturn80file0L4-L35 fileciteturn80file0L37-L41

## 01. Two Sum

**Question:** Given an array and a target, find two numbers that add up to the target.

**Primary pattern:** Hash Map.

**Recognition clue:** You need to remember previously seen values so that the required complement can be found quickly.

**Think about:** `target - current`.

**Mastery checkpoint:** Explain why a nested-loop solution is slower and what information a hash map stores.

---

## 02. Valid Parentheses

**Question:** Determine whether brackets close in the correct order.

**Primary pattern:** Stack.

**Recognition clue:** The most recently opened bracket must be matched first.

**Think about:** Last opened → first closed.

**Mastery checkpoint:** Explain why a queue is the wrong data structure.

---

## 03. Merge Two Sorted Lists

**Question:** Combine two sorted linked lists into one sorted linked list.

**Primary pattern:** Linked List basics.

**Recognition clue:** Both inputs are already sorted, so compare the current nodes and advance the smaller one.

**Think about:** Two current pointers.

**Mastery checkpoint:** Explain pointer movement without losing either list.

---

## 04. Best Time to Buy and Sell Stock

**Question:** Find the maximum profit obtainable from stock prices.

**Primary pattern:** Array / Min-Max tracking.

**Recognition clue:** For each price, you care about the smallest earlier buying price and the best profit so far.

**Think about:** Running minimum + running best.

**Mastery checkpoint:** Solve it in one pass.

---

## 05. Valid Palindrome

**Question:** Determine whether a string reads the same forward and backward while ignoring spaces.

**Primary pattern:** Two Pointers.

**Recognition clue:** Compare matching characters from opposite ends.

**Think about:** Left pointer + right pointer.

**Mastery checkpoint:** Handle spaces and character normalization correctly.

---

## 06. Invert a Binary Tree

**Question:** Flip a binary tree left to right.

**Primary pattern:** Tree basics / Recursion.

**Recognition clue:** Every node needs its left and right children exchanged.

**Think about:** Solve the same operation on each subtree.

**Mastery checkpoint:** Explain the recursive base case.

---

## 07. Valid Anagram

**Question:** Check whether two words contain exactly the same letters with the same frequencies.

**Primary pattern:** Frequency Counting.

**Recognition clue:** The order does not matter; frequencies do.

**Think about:** Character → count.

**Mastery checkpoint:** Explain why comparing frequencies is enough.

---

## 08. Binary Search

**Question:** Find an item efficiently in a sorted array.

**Primary pattern:** Divide and Conquer.

**Recognition clue:** The input is sorted and each comparison can eliminate half the search space.

**Think about:** Middle element + search boundaries.

**Mastery checkpoint:** Derive `O(log n)` rather than memorizing it.

---

## 09. Reverse a Linked List

**Question:** Reverse the direction of a linked list.

**Primary pattern:** Pointer manipulation.

**Recognition clue:** Each node's next pointer must be redirected without losing the remaining list.

**Think about:** Previous / current / next.

**Mastery checkpoint:** Explain exactly when each pointer moves.

---

## 10. Contains Duplicate

**Question:** Determine whether any value appears more than once.

**Primary pattern:** Set / Hash Set.

**Recognition clue:** You only need to know whether a value has appeared before.

**Think about:** Seen values.

**Mastery checkpoint:** Compare set-based and sorting-based approaches.

---

## 11. Maximum Subarray

**Question:** Find the contiguous subarray with the largest sum.

**Primary pattern:** Kadane's Algorithm.

**Recognition clue:** At each position, decide whether continuing the previous subarray is better than starting fresh.

**Think about:** Best ending here vs best overall.

**Mastery checkpoint:** Explain why negative running sums can be discarded.

---

## 12. Climbing Stairs

**Question:** Count the ways to reach the top when you can take 1 or 2 steps.

**Primary pattern:** Basic Dynamic Programming.

**Recognition clue:** The answer for step `n` depends on smaller previously solved steps.

**Think about:** `ways(n) = ways(n-1) + ways(n-2)`.

**Mastery checkpoint:** Explain the base cases and why storing only two previous values is enough.

---

## 13. Linked List Cycle

**Question:** Detect whether a linked list loops back on itself.

**Primary pattern:** Fast & Slow Pointers.

**Recognition clue:** A cycle can be detected by moving two pointers at different speeds.

**Think about:** Runner vs walker.

**Mastery checkpoint:** Explain why two pointers eventually meet inside a cycle.

---

## 14. Missing Number

**Question:** Find the missing number from a sequence containing values from `0` to `n`.

**Primary pattern:** Bit Manipulation / Math.

**Recognition clue:** The expected set has a known mathematical/XOR relationship.

**Think about:** Expected information minus observed information.

**Mastery checkpoint:** Know at least one `O(n)` / `O(1)` approach and why it works.

---

## 15. Majority Element

**Question:** Find the element appearing more than `n/2` times.

**Primary pattern:** Boyer-Moore Voting.

**Recognition clue:** One value has a strict majority, so competing values can cancel each other.

**Think about:** Candidate + balance.

**Mastery checkpoint:** Explain the cancellation intuition.

---

## 16. Palindrome Number

**Question:** Determine whether an integer reads the same forward and backward.

**Primary pattern:** Math.

**Recognition clue:** Reverse or compare digits without converting the entire number to a string.

**Think about:** Digit extraction.

**Mastery checkpoint:** Handle negative values and trailing zero behavior.

---

## 17. Same Tree

**Question:** Determine whether two binary trees are structurally identical with equal values.

**Primary pattern:** Tree DFS.

**Recognition clue:** The same comparison must be recursively applied to corresponding nodes.

**Think about:** Current node + left subtree + right subtree.

**Mastery checkpoint:** Identify all base cases.

---

## 18. Maximum Depth of Binary Tree

**Question:** Find the longest path from the root to a leaf.

**Primary pattern:** Tree BFS/DFS.

**Recognition clue:** Every subtree contributes one level plus its deeper child subtree.

**Think about:** `1 + max(left, right)`.

**Mastery checkpoint:** Solve with DFS and understand the BFS alternative.

---

## 19. Single Number

**Question:** Find the value appearing once when every other value appears twice.

**Primary pattern:** Bitwise XOR.

**Recognition clue:** Duplicate pairs should cancel while the unique value remains.

**Think about:** `x ^ x = 0` and `x ^ 0 = x`.

**Mastery checkpoint:** Explain why order does not matter for XOR here.

---

## 20. Move Zeroes

**Question:** Move all zeroes to the end while keeping the relative order of non-zero elements.

**Primary pattern:** Two Pointers.

**Recognition clue:** One pointer tracks where the next non-zero value belongs.

**Think about:** Write position vs scanning position.

**Mastery checkpoint:** Do it in-place.

---

## 21. Squares of a Sorted Array

**Question:** Square every value in a sorted array and return the squared values in sorted order.

**Primary pattern:** Two Pointers.

**Recognition clue:** Negative values can produce large squares, so compare magnitudes from both ends.

**Think about:** Largest absolute value is at one of the ends.

**Mastery checkpoint:** Avoid sorting the squared result when possible.

---

## 22. Remove Duplicates from Sorted Array

**Question:** Remove duplicates in-place from a sorted array.

**Primary pattern:** Two Pointers.

**Recognition clue:** Because the array is sorted, duplicates are adjacent.

**Think about:** Read pointer + write pointer.

**Mastery checkpoint:** Explain why a single scan is enough.

---

## 23. Fizz Buzz

**Question:** Produce the required representation for each number based on divisibility.

**Primary pattern:** Basic Logic.

**Recognition clue:** Iterate once and apply mutually exclusive divisibility rules in the correct order.

**Think about:** Combined condition before individual conditions.

**Mastery checkpoint:** Avoid incorrect ordering of the divisibility checks.

---

## 24. Fibonacci Number

**Question:** Compute the N-th Fibonacci number.

**Primary pattern:** Recursion / Math.

**Recognition clue:** Each value depends on the previous two values.

**Think about:** Repeated subproblems and iterative state.

**Mastery checkpoint:** Compare naive recursion with iterative/DP approaches.

---

## 25. Intersection of Two Arrays II

**Question:** Find common elements between two arrays, including duplicates.

**Primary pattern:** Hash Map / Sorting.

**Recognition clue:** You need frequencies, not just membership.

**Think about:** Count available copies.

**Mastery checkpoint:** Explain both frequency-map and sorting approaches.

---

## 26. First Unique Character in a String

**Question:** Find the index of the first non-repeating character.

**Primary pattern:** Frequency Map.

**Recognition clue:** You need frequency information before deciding which character is first unique.

**Think about:** Count first, scan second.

**Mastery checkpoint:** Explain why one pass alone is not enough with a simple frequency map.

---

## 27. Pascal's Triangle

**Question:** Generate the first `N` rows of Pascal's Triangle.

**Primary pattern:** Array simulation.

**Recognition clue:** Interior values are produced from two values directly above them.

**Think about:** Previous row → current row.

**Mastery checkpoint:** Correctly handle row boundaries.

---

## 28. Valid Perfect Square

**Question:** Determine whether a number is a perfect square without using a library square-root function.

**Primary pattern:** Binary Search.

**Recognition clue:** Squared values grow monotonically, giving a searchable numeric range.

**Think about:** Search for an integer whose square equals the target.

**Mastery checkpoint:** Avoid overflow-style mistakes conceptually when multiplying.

---

## 29. Symmetric Tree

**Question:** Determine whether a binary tree is a mirror image of itself.

**Primary pattern:** Tree Recursion.

**Recognition clue:** Compare opposite children recursively: left of one side with right of the other.

**Think about:** Mirror pairs.

**Mastery checkpoint:** Distinguish this from Same Tree.

---

## 30. Min Stack

**Question:** Design a stack that supports retrieving the minimum element in `O(1)` time.

**Primary pattern:** Stack design.

**Recognition clue:** Normal stack operations are not enough if minimum retrieval scans the stack.

**Think about:** Store enough minimum-state information as values are pushed/popped.

**Mastery checkpoint:** Every required operation must meet its target complexity.

---

## 31. Reverse String

**Question:** Reverse an array of characters in-place.

**Primary pattern:** Two Pointers.

**Recognition clue:** This is the same opposite-end swapping pattern used in our `reverse_array` practice.

**Think about:** Left ↔ right.

**Mastery checkpoint:** Recognize the pattern immediately from the wording “in-place reverse”.

---

## 32. Happy Number

**Question:** Determine whether repeatedly replacing a number by the sum of the squares of its digits eventually reaches `1`.

**Primary pattern:** Cycle Detection.

**Recognition clue:** Repeated transformation can revisit a previous state, creating a cycle.

**Think about:** State → next state.

**Mastery checkpoint:** Identify how cycle detection applies even though this is not a linked list.

---

## 33. Merge Sorted Array

**Question:** Merge two sorted arrays in-place.

**Primary pattern:** Two Pointers from the end.

**Recognition clue:** Writing from the front can overwrite useful values; the back provides safe space.

**Think about:** Largest remaining values first.

**Mastery checkpoint:** Explain why the pointers move backward.

---

## 34. Subtree of Another Tree

**Question:** Determine whether one binary tree appears as a subtree of another.

**Primary pattern:** Tree Matching.

**Recognition clue:** At each candidate node, test whether the two trees are identical from that point.

**Think about:** Search candidate roots + same-tree comparison.

**Mastery checkpoint:** Separate “find candidate” from “compare trees”.

---

# Phase 2 — Medium Problems

The source lists problems 35–74 as Medium. fileciteturn80file0L42-L72 fileciteturn80file0L74-L84

## 35. Longest Substring Without Repeating Characters

**Pattern:** Sliding Window.

**Question:** Find the longest substring containing no repeated characters.

**Recognition clue:** You need the longest valid contiguous region while maintaining a uniqueness constraint.

**Think about:** Expand right, shrink left when invalid.

**Mastery checkpoint:** Know exactly when the left boundary moves.

---

## 36. Container With Most Water

**Pattern:** Two Pointers.

**Question:** Find two lines that hold the maximum possible water.

**Recognition clue:** The area depends on width and the smaller boundary; moving the taller boundary cannot improve the limiting height for the same width.

**Think about:** Start at both ends and move the shorter side.

**Mastery checkpoint:** Explain why the pointer movement is safe.

---

## 37. 3Sum

**Pattern:** Sorting + Two Pointers.

**Question:** Find all unique triplets whose sum is zero.

**Recognition clue:** Fix one value, then solve a two-sum-style problem on the remaining sorted portion.

**Think about:** Sort → fix → two pointers → skip duplicates.

**Mastery checkpoint:** Explain both duplicate handling and complexity.

---

## 38. Group Anagrams

**Pattern:** Hash Map categorization.

**Question:** Group words containing the same letters.

**Recognition clue:** Different words need the same canonical key when they have identical character frequencies.

**Think about:** Signature/key → list of words.

**Mastery checkpoint:** Compare sorted-string keys with frequency keys.

---

## 39. Product of Array Except Self

**Pattern:** Prefix/Suffix arrays.

**Question:** For every position, compute the product of all other values without division.

**Recognition clue:** Everything except the current index splits naturally into a prefix and suffix.

**Think about:** Product before + product after.

**Mastery checkpoint:** Achieve constant extra space apart from the output if required.

---

## 40. Find All Anagrams in a String

**Pattern:** Sliding Window + Hash Map.

**Question:** Locate all windows that are anagrams of a target string.

**Recognition clue:** Fixed-size contiguous windows plus frequency equality.

**Think about:** Add right character, remove left character.

**Mastery checkpoint:** Maintain the window counts incrementally.

---

## 41. Remove Nth Node From End of List

**Pattern:** Two Pointers.

**Question:** Remove a linked-list node counted from the end.

**Recognition clue:** The distance from the end can be converted into a fixed gap between two pointers.

**Think about:** Maintain an `n`-node gap.

**Mastery checkpoint:** Handle removing the head cleanly.

---

## 42. Copy List with Random Pointer

**Pattern:** Hash Map.

**Question:** Deep-copy a linked list whose nodes have next and random pointers.

**Recognition clue:** A copied node must correspond exactly to each original node, including random references.

**Think about:** Original node → copied node mapping.

**Mastery checkpoint:** Explain why the mapping prevents duplicate copies.

---

## 43. Binary Tree Level Order Traversal

**Pattern:** BFS.

**Question:** Traverse a binary tree level by level.

**Recognition clue:** Nodes must be processed in distance-from-root order.

**Think about:** Queue.

**Mastery checkpoint:** Know how to separate one level from the next.

---

## 44. Lowest Common Ancestor of a Binary Tree

**Pattern:** Tree DFS.

**Question:** Find the lowest node that is an ancestor of two target nodes.

**Recognition clue:** A subtree can report whether it contains either target and combine the reports.

**Think about:** Left result + right result + current node.

**Mastery checkpoint:** Understand why finding targets in both sides identifies the LCA.

---

## 45. Kth Largest Element in an Array

**Pattern:** Heap / Priority Queue.

**Question:** Find the K-th largest value without fully sorting the array.

**Recognition clue:** You only need to maintain the best `k` candidates rather than all elements in sorted order.

**Think about:** Size-`k` heap.

**Mastery checkpoint:** Explain why the heap size remains bounded.

---

## 46. Top K Frequent Elements

**Pattern:** Heap or Bucket Sort.

**Question:** Find the `k` most frequent items.

**Recognition clue:** First determine frequencies, then select the highest-frequency items.

**Think about:** Frequency map + bounded selection.

**Mastery checkpoint:** Compare heap and bucket approaches.

---

## 47. Course Schedule

**Pattern:** Graph Cycle Detection / Topological Sort.

**Question:** Determine whether all courses can be completed given prerequisite relationships.

**Recognition clue:** Prerequisites form directed dependencies; a cycle makes completion impossible.

**Think about:** Directed graph + cycle detection.

**Mastery checkpoint:** Solve using either DFS cycle detection or indegree/topological sorting.

---

## 48. Number of Islands

**Pattern:** Graph BFS/DFS.

**Question:** Count connected groups of land in a grid.

**Recognition clue:** Each unvisited land cell can start a traversal that marks one entire island.

**Think about:** Grid as a graph.

**Mastery checkpoint:** Handle visited cells correctly.

---

## 49. Clone Graph

**Pattern:** Graph traversal.

**Question:** Deep-copy an entire graph.

**Recognition clue:** Cycles mean a node may be encountered more than once, so original-to-copy mapping is required.

**Think about:** DFS/BFS + map.

**Mastery checkpoint:** Explain why cloning without a map can recurse forever or duplicate nodes.

---

## 50. Coin Change

**Pattern:** Dynamic Programming.

**Question:** Find the minimum number of coins needed to make a target amount.

**Recognition clue:** The best answer for an amount depends on answers for smaller amounts.

**Think about:** `dp[amount]` from `dp[amount - coin]`.

**Mastery checkpoint:** Define the state and impossible-state representation.

---

## 51. Longest Common Subsequence

**Pattern:** Dynamic Programming.

**Question:** Find the longest subsequence shared by two strings.

**Recognition clue:** Two sequences create a two-dimensional state based on prefixes of both strings.

**Think about:** Match → diagonal; mismatch → best of two directions.

**Mastery checkpoint:** Distinguish subsequence from substring.

---

## 52. Subarray Sum Equals K

**Pattern:** Prefix Sum + Hash Map.

**Question:** Count continuous subarrays whose sum equals `k`.

**Recognition clue:** A subarray sum can be represented as the difference between two prefix sums.

**Think about:** If current prefix is `S`, look for earlier `S-k`.

**Mastery checkpoint:** Store prefix-sum frequencies, not just membership.

---

## 53. Search in Rotated Sorted Array

**Pattern:** Modified Binary Search.

**Question:** Search efficiently in a sorted array that has been rotated.

**Recognition clue:** At least one side of the midpoint remains sorted.

**Think about:** Identify the sorted half, then decide which half can contain the target.

**Mastery checkpoint:** Preserve `O(log n)` behavior.

---

## 54. Validate Binary Search Tree

**Pattern:** Tree boundaries.

**Question:** Determine whether a binary tree obeys BST ordering rules.

**Recognition clue:** A node's valid range is constrained by all of its ancestors, not only its direct parent.

**Think about:** Lower bound + upper bound.

**Mastery checkpoint:** Avoid the common “compare only with children” mistake.

---

## 55. Add Two Numbers

**Pattern:** Linked List math.

**Question:** Add two numbers represented by linked lists whose digits are stored in reverse order.

**Recognition clue:** Addition proceeds digit by digit just like elementary arithmetic.

**Think about:** Current digits + carry.

**Mastery checkpoint:** Handle different list lengths and final carry.

---

## 56. String to Integer (atoi)

**Pattern:** String parsing.

**Question:** Implement conversion from a string to an integer under specified parsing rules.

**Recognition clue:** The challenge is stateful parsing: whitespace, sign, digits, stopping conditions, and bounds.

**Think about:** Parser state machine.

**Mastery checkpoint:** Define the exact order of parsing decisions.

---

## 57. Spiral Matrix

**Pattern:** Matrix simulation.

**Question:** Return matrix elements in spiral order.

**Recognition clue:** The traversal direction changes after reaching a current boundary.

**Think about:** Top, bottom, left, right boundaries.

**Mastery checkpoint:** Prevent revisiting the center row/column.

---

## 58. Word Search

**Pattern:** Backtracking / DFS.

**Question:** Determine whether a word can be formed by stepping through adjacent grid cells.

**Recognition clue:** Each choice affects the remaining search, and cells cannot be reused in the same path.

**Think about:** Choose → explore → undo.

**Mastery checkpoint:** Restore the cell state during backtracking.

---

## 59. House Robber

**Pattern:** Dynamic Programming.

**Question:** Maximize the value robbed without taking adjacent houses.

**Recognition clue:** At each house, choose between taking it plus the best non-adjacent result or skipping it.

**Think about:** Take vs skip.

**Mastery checkpoint:** Derive the recurrence before coding.

---

## 60. Pacific Atlantic Water Flow

**Pattern:** Graph DFS/BFS.

**Question:** Find cells from which water can reach both oceans.

**Recognition clue:** Reverse the flow: start from ocean boundaries and traverse cells that could flow into the ocean.

**Think about:** Reverse reachability.

**Mastery checkpoint:** Understand why starting from the oceans is more efficient than starting from every cell.

---

## 61. Generate Parentheses

**Pattern:** Backtracking.

**Question:** Generate all combinations of well-formed parentheses.

**Recognition clue:** Choices are constrained by how many opening and closing parentheses remain valid.

**Think about:** Open count vs close count.

**Mastery checkpoint:** Never allow the partial sequence to become invalid.

---

## 62. Permutations

**Pattern:** Backtracking.

**Question:** Generate every ordering of a set of distinct numbers.

**Recognition clue:** Each position chooses one unused value.

**Think about:** Choose → recurse → undo.

**Mastery checkpoint:** Track which values are already used.

---

## 63. Subsets

**Pattern:** Backtracking / Bitmasking.

**Question:** Generate the power set of the input values.

**Recognition clue:** Every element creates a binary decision: include or exclude.

**Think about:** Two branches per element.

**Mastery checkpoint:** Explain why there are `2^n` subsets.

---

## 64. Decode Ways

**Pattern:** Dynamic Programming.

**Question:** Count how many valid letter decodings correspond to a digit string.

**Recognition clue:** At each position, a valid decoding may use one digit or a valid two-digit combination.

**Think about:** One-step vs two-step transitions.

**Mastery checkpoint:** Handle zero correctly.

---

## 65. Unique Paths

**Pattern:** Combinatorics / DP.

**Question:** Count paths from the top-left to bottom-right of a grid using allowed moves.

**Recognition clue:** The number of ways to reach a cell comes from its valid predecessor cells.

**Think about:** Grid DP.

**Mastery checkpoint:** Recognize the relationship to Pascal's Triangle.

---

## 66. Sort Colors

**Pattern:** Dutch National Flag Algorithm.

**Question:** Sort an array containing only `0`, `1`, and `2` in-place.

**Recognition clue:** There are only three categories, so maintain regions for each category.

**Think about:** Low / middle / high pointers.

**Mastery checkpoint:** Explain the invariant for each region.

---

## 67. K Closest Points to Origin

**Pattern:** Heap / Max Heap.

**Question:** Find the `k` points closest to the origin.

**Recognition clue:** You need only the best `k` candidates, so maintain a bounded heap.

**Think about:** Distance ranking without unnecessary full sorting.

**Mastery checkpoint:** Use squared distance when the square root is unnecessary.

---

## 68. Longest Palindromic Substring

**Pattern:** DP / Expand Around Center.

**Question:** Find the longest palindromic contiguous substring.

**Recognition clue:** Every palindrome has a center; expand while characters match.

**Think about:** Odd center + even center.

**Mastery checkpoint:** Understand why substring means contiguous.

---

## 69. Gas Station

**Pattern:** Greedy.

**Question:** Determine the starting station that allows a complete circular trip.

**Recognition clue:** If the running fuel becomes negative at a station, none of the earlier candidates can be a valid start under the greedy invariant.

**Think about:** Running balance + total balance.

**Mastery checkpoint:** Explain why one candidate can be discarded for an entire prefix.

---

## 70. Rotting Oranges

**Pattern:** Graph BFS.

**Question:** Find the minimum time required for all reachable fresh oranges to rot.

**Recognition clue:** Rot spreads simultaneously one layer at a time.

**Think about:** Multi-source BFS.

**Mastery checkpoint:** Track levels/time correctly and detect unreachable fresh oranges.

---

## 71. Daily Temperatures

**Pattern:** Monotonic Stack.

**Question:** For each day, find how many days until a warmer temperature.

**Recognition clue:** Unresolved previous temperatures can be represented by a monotonic stack of indices.

**Think about:** Current temperature resolves smaller previous temperatures.

**Mastery checkpoint:** Store indices, not just values.

---

## 72. Design Circular Queue

**Pattern:** Design / Array.

**Question:** Implement a fixed-capacity circular queue.

**Recognition clue:** The end of the backing array should wrap around to the beginning.

**Think about:** Head, tail, size/capacity.

**Mastery checkpoint:** Define empty and full states unambiguously.

---

## 73. Construct Binary Tree from Preorder and Inorder Traversal

**Pattern:** Tree Recursion.

**Question:** Reconstruct a unique binary tree from preorder and inorder traversals.

**Recognition clue:** Preorder identifies the root first; inorder tells how the left and right subtrees split.

**Think about:** Root position + recursive ranges.

**Mastery checkpoint:** Use a value-to-index map for efficient splits.

---

## 74. Partition Equal Subset Sum

**Pattern:** Knapsack DP.

**Question:** Determine whether the array can be divided into two subsets with equal sums.

**Recognition clue:** Equal partition is equivalent to finding a subset that reaches half the total sum.

**Think about:** 0/1 knapsack target.

**Mastery checkpoint:** Recognize when the target is impossible immediately because of total-sum parity.

---

# Phase 3 — Hard Problems

The source lists problems 75–100 as Hard. fileciteturn80file0L85-L109 fileciteturn80file0L111-L117

These are **not** our immediate practice targets. We will reach them only after the corresponding patterns are strong enough.

## 75. Median of Two Sorted Arrays

**Pattern:** Advanced Binary Search.

**Question:** Find the median of two sorted arrays in logarithmic time.

**Recognition clue:** The arrays are sorted and the required complexity forces a partition-based binary-search solution.

**Think about:** Partition both arrays so the left halves contain the correct number of elements.

**Mastery checkpoint:** Derive the partition invariant before coding.

---

## 76. Trapping Rain Water

**Pattern:** Two Pointers / Monotonic Stack.

**Question:** Calculate the total water trapped between elevation bars.

**Recognition clue:** Water at a position depends on boundaries on both sides; two pointers can maintain enough boundary information.

**Think about:** Lower boundary determines which side can be resolved.

**Mastery checkpoint:** Explain the invariant behind the pointer movement.

---

## 77. Merge k Sorted Lists

**Pattern:** Heap / Priority Queue.

**Question:** Merge many sorted linked lists into one sorted list.

**Recognition clue:** At any moment, only the smallest current node from each list is relevant.

**Think about:** Min-heap of current heads.

**Mastery checkpoint:** Keep the heap bounded by the number of lists.

---

## 78. Reverse Nodes in k-Group

**Pattern:** Advanced Linked List pointers.

**Question:** Reverse linked-list nodes in groups of size `k`.

**Recognition clue:** Reuse the reverse-list pointer technique, but apply it to bounded segments.

**Think about:** Locate group → reverse group → reconnect.

**Mastery checkpoint:** Never lose the next group.

---

## 79. Edit Distance

**Pattern:** Matrix Dynamic Programming.

**Question:** Find the minimum edits required to transform one word into another.

**Recognition clue:** Prefixes of both strings define a two-dimensional state; each step can insert, delete, or replace.

**Think about:** DP matrix over prefixes.

**Mastery checkpoint:** Derive the three transition choices.

---

## 80. Longest Consecutive Sequence

**Pattern:** Hash Set.

**Question:** Find the longest consecutive sequence in an unsorted array in `O(n)` time.

**Recognition clue:** Sorting would violate the target complexity; a set can test whether sequence neighbors exist in constant average time.

**Think about:** Start only at numbers with no predecessor.

**Mastery checkpoint:** Explain why each sequence is effectively scanned once.

---

## 81. Sliding Window Maximum

**Pattern:** Deque / Monotonic Queue.

**Question:** Find the maximum value in every fixed-size moving window.

**Recognition clue:** The maximum of overlapping windows can be maintained without rescanning each window.

**Think about:** Decreasing deque of useful indices.

**Mastery checkpoint:** Remove expired indices and dominated values.

---

## 82. Minimum Window Substring

**Pattern:** Advanced Sliding Window.

**Question:** Find the smallest substring containing all required target characters.

**Recognition clue:** Expand until valid, then shrink while validity is preserved.

**Think about:** Required counts + formed counts.

**Mastery checkpoint:** Know exactly when a window becomes valid and invalid.

---

## 83. Word Ladder

**Pattern:** Graph Shortest Path / BFS.

**Question:** Find the shortest transformation sequence between words when one letter changes at a time.

**Recognition clue:** Every valid one-letter transformation is an edge; shortest number of transformations means BFS.

**Think about:** Implicit graph + level-order search.

**Mastery checkpoint:** Avoid exploring equivalent transformations repeatedly.

---

## 84. Serialize and Deserialize Binary Tree

**Pattern:** Tree design.

**Question:** Convert a binary tree into a string and reconstruct the same tree from that representation.

**Recognition clue:** The representation must preserve structure as well as values.

**Think about:** Traversal + explicit null markers.

**Mastery checkpoint:** Ensure serialization is unambiguous.

---

## 85. Find Median from Data Stream

**Pattern:** Two Heaps.

**Question:** Continuously maintain the median as numbers arrive.

**Recognition clue:** Split the stream into a lower half and upper half while keeping the halves balanced.

**Think about:** Max-heap lower half + min-heap upper half.

**Mastery checkpoint:** Maintain the size and ordering invariants after every insertion.

---

## 86. Binary Tree Maximum Path Sum

**Pattern:** Tree Post-order traversal.

**Question:** Find the maximum-sum path anywhere in a binary tree.

**Recognition clue:** A node can return the best downward contribution to its parent while separately updating a global path through the node.

**Think about:** Local contribution vs global answer.

**Mastery checkpoint:** Handle negative contributions correctly.

---

## 87. Regular Expression Matching

**Pattern:** Dynamic Programming / Backtracking.

**Question:** Match a string using a custom pattern containing `.` and `*`.

**Recognition clue:** `*` creates a choice between consuming a character and consuming zero characters, producing overlapping subproblems.

**Think about:** State `(string index, pattern index)`.

**Mastery checkpoint:** Carefully distinguish zero occurrences from one-or-more occurrences.

---

## 88. N-Queens

**Pattern:** Backtracking.

**Question:** Place queens so that no two queens attack each other.

**Recognition clue:** Each row requires a choice, and invalid partial placements can be abandoned immediately.

**Think about:** Columns + diagonals as constraints.

**Mastery checkpoint:** Use sets or equivalent state to test attacks efficiently.

---

## 89. Burst Balloons

**Pattern:** Matrix Chain Multiplication DP.

**Question:** Choose an order for bursting balloons that maximizes the score.

**Recognition clue:** The order affects future neighbors, so choose the final balloon in an interval rather than the first.

**Think about:** Interval DP.

**Mastery checkpoint:** Derive why choosing the last action simplifies the transition.

---

## 90. Largest Rectangle in Histogram

**Pattern:** Monotonic Stack.

**Question:** Find the largest rectangular area under a histogram.

**Recognition clue:** Each bar needs the nearest smaller boundary on both sides.

**Think about:** Increasing stack of indices.

**Mastery checkpoint:** Understand when a bar's maximal rectangle becomes fully determined.

---

## 91. Maximal Rectangle

**Pattern:** DP / Histogram base.

**Question:** Find the largest all-ones rectangle in a binary matrix.

**Recognition clue:** Convert each row into a histogram of consecutive heights and reuse the histogram rectangle problem.

**Think about:** Row-by-row histogram transformation.

**Mastery checkpoint:** Connect two previously learned patterns rather than treating this as a completely new problem.

---

## 92. First Missing Positive

**Pattern:** Cyclic Sort.

**Question:** Find the smallest missing positive integer in `O(n)` time and `O(1)` space.

**Recognition clue:** Values that belong in positions `1..n` can be placed at their corresponding indexes.

**Think about:** Value `x` belongs near index `x-1`.

**Mastery checkpoint:** Handle out-of-range values and duplicates without extra storage.

---

## 93. Binary Tree Postorder Traversal (Iterative)

**Pattern:** Stack manipulation.

**Question:** Perform postorder traversal without recursion.

**Recognition clue:** Postorder requires left and right processing before the node, so explicit stack state is needed.

**Think about:** Simulate recursion with a stack.

**Mastery checkpoint:** Understand when a node is ready to be output.

---

## 94. Word Search II

**Pattern:** Trie + Backtracking.

**Question:** Find all dictionary words hidden in a character grid.

**Recognition clue:** Many words share prefixes, so a trie can prune impossible paths while DFS explores the grid.

**Think about:** Trie-guided grid backtracking.

**Mastery checkpoint:** Combine two data structures/patterns rather than solving each word independently.

---

## 95. Alien Dictionary

**Pattern:** Graph / Topological Sort.

**Question:** Derive the ordering of an unknown alphabet from a sorted dictionary.

**Recognition clue:** The first differing characters of adjacent words create directed ordering constraints.

**Think about:** Characters as graph nodes; constraints as edges.

**Mastery checkpoint:** Detect invalid prefix ordering and cycles.

---

## 96. Longest Valid Parentheses

**Pattern:** DP / Stack.

**Question:** Find the length of the longest well-formed parentheses substring.

**Recognition clue:** Validity depends on matching opening positions with closing positions while preserving contiguous length.

**Think about:** Stack indices or DP lengths.

**Mastery checkpoint:** Understand how a valid segment's starting boundary is tracked.

---

## 97. Minimum Window Subsequence

**Pattern:** Dynamic Programming / Two Pointers.

**Question:** Find the smallest window in one string that contains another string as a subsequence.

**Recognition clue:** Unlike substring matching, target characters must appear in order but do not need to be adjacent.

**Think about:** Find a valid end, then shrink backward/forward to minimize.

**Mastery checkpoint:** Distinguish subsequence constraints from substring constraints.

---

## 98. Employee Free Time

**Pattern:** Interval Heap / Sorting.

**Question:** Find time intervals when all employees are free.

**Recognition clue:** Merge overlapping schedules and inspect the gaps between merged intervals.

**Think about:** Sort by start time or maintain the next interval with a heap.

**Mastery checkpoint:** Clearly define whether touching intervals create a gap.

---

## 99. Maximum Profit in Job Scheduling

**Pattern:** DP + Binary Search.

**Question:** Select non-overlapping jobs to maximize total profit.

**Recognition clue:** Each job creates a take/skip decision, and the next compatible job can be found by binary search after sorting.

**Think about:** Sort by end time + previous compatible job + DP.

**Mastery checkpoint:** Define the DP state around the sorted jobs.

---

## 100. Smallest Sufficient Team

**Pattern:** Bitmask Dynamic Programming.

**Question:** Find the smallest team whose combined skills cover all required skills.

**Recognition clue:** A limited set of required skills can be represented as bits, making team selection a state-transition problem.

**Think about:** Skill mask + minimum team for each mask.

**Mastery checkpoint:** Understand why bitmasks compactly represent the set of covered skills.

---

# Pattern Recognition Index

Use this section when reviewing rather than memorizing individual solutions.

| Pattern | Problems to Recognize |
|---|---|
| Hash Map / Frequency | 1, 7, 25, 26, 38, 40, 42, 46, 52 |
| Set / Hash Set | 10, 80 |
| Stack | 2, 30, 71, 90, 96 |
| Two Pointers | 5, 20, 21, 22, 31, 33, 36, 37, 76, 97 |
| Fast / Slow Pointers | 13 |
| Sliding Window | 35, 40, 82 |
| Binary Search | 8, 28, 53, 75, 99 |
| Linked List | 3, 9, 41, 42, 55, 77, 78 |
| Tree DFS / Recursion | 6, 17, 18, 29, 34, 44, 54, 73, 84, 86, 93 |
| BFS / Graph Traversal | 43, 47, 48, 49, 60, 70, 83, 95 |
| Dynamic Programming | 12, 24, 39, 50, 51, 59, 64, 65, 68, 74, 79, 87, 89, 91, 96, 97, 99, 100 |
| Backtracking | 58, 61, 62, 63, 87, 88, 94 |
| Heap / Priority Queue | 45, 46, 67, 77, 85, 98 |
| Monotonic Stack / Queue | 71, 81, 90, 91 |
| Greedy | 15, 69 |
| Prefix Sum | 39, 52 |
| Bit Manipulation | 14, 19, 100 |
| Matrix / Grid | 48, 57, 58, 60, 65, 70, 91 |
| Interval / Scheduling | 69, 98, 99 |

> The pattern names above preserve the primary classifications in the supplied PDF; the additional recognition clues are our study guidance built around those classifications. fileciteturn80file0L5-L35 fileciteturn80file0L43-L72 fileciteturn80file0L76-L84 fileciteturn80file0L86-L109

# How This Fits Our Repository

Our repository already separates:

```text
roadmap/
topics/
practice/
revision/
progress/
templates/
tests/
```

We will use this roadmap as the **master problem-recognition curriculum**.

The individual solved problems belong in the relevant `topics/` folders. The roadmap should remain solution-light so that it can be used as a recognition test.

For example, our current Array/Easy progression is:

```text
topics/01-arrays/easy/
├── find_maximum.py
├── find_maximum.md
├── find_minimum.py
├── find_minimum.md
├── linear_search.py
├── linear_search.md
├── count_occurrences.py
├── count_occurrences.md
├── second_largest.py
├── second_largest.md
├── reverse_array.py
└── reverse_array.md
```

These foundational exercises are intentionally used before jumping directly into the 100 curated problems. They train the underlying skills needed to recognize the patterns in the roadmap.

# Mastery Protocol

For each new problem we will follow this process:

### Stage 1 — Recognition

Read only the problem and identify the likely pattern.

### Stage 2 — Constraints

Ask what the input properties allow us to exploit:

```text
Sorted?
Contiguous?
Duplicates?
Fixed window?
Dependencies?
Tree structure?
Graph relationships?
Need O(1) extra space?
Need O(log n)?
```

### Stage 3 — Algorithm Design

Explain the algorithm in plain English before writing code.

### Stage 4 — Implementation

Write the solution yourself.

### Stage 5 — Testing

Test:

```text
Normal case
Smallest valid input
Empty input when applicable
Duplicates
Negative values when applicable
Already sorted / reverse sorted when applicable
Boundary conditions
```

### Stage 6 — Complexity

State:

```text
Time = ?
Space = ?
```

and explain why.

### Stage 7 — Documentation

Write what **I learned**, including mistakes and the pattern that solved the problem.

### Stage 8 — Reattempt

After a gap, solve the problem again without opening the implementation.

# Current Position

We have already completed six foundational Array/Easy exercises:

```text
01. Find Maximum
02. Find Minimum
03. Linear Search
04. Count Occurrences
05. Second Largest Distinct
06. Reverse Array
```

We are currently beginning the next foundational problem:

```text
07. Check if an Array is Sorted
```

The goal is not to rush toward Problem 100. The goal is to make the patterns become recognizable enough that the wording of a new problem starts suggesting the correct data structure or algorithm automatically.

# Important Principle

**Do not memorize the answer. Memorize the signal that tells you which pattern to consider.**

Examples:

```text
"sorted array" + "find efficiently"
        → Binary Search

"longest contiguous" + constraint
        → Sliding Window

"appears how many times"
        → Frequency Map / Counting

"previously seen"
        → Hash Set / Hash Map

"opposite ends"
        → Two Pointers

"last opened, first closed"
        → Stack

"shortest path in unweighted graph"
        → BFS

"all combinations"
        → Backtracking

"best answer from smaller subproblems"
        → Dynamic Programming

"keep top/bottom K"
        → Heap / Priority Queue
```

The 100 problems are therefore a **pattern-recognition curriculum**, not simply a list of 100 coding exercises.
