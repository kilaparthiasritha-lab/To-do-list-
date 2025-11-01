# Instruction Rearrangement Problem

## Problem Description

Given two lists of instructions (shuffled and original), find the minimum number of "cut and insert" operations needed to transform the shuffled list into the original list.

An operation consists of:
- Cutting one or more consecutive instructions from the shuffled list
- Inserting them at a new position

Consecutive instructions can be moved together in a single operation **only if** they are also consecutive in the target (original) list.

## Solution Approach

The solution uses the **Longest Increasing Subsequence (LIS)** algorithm:

1. **Map positions**: Convert each instruction in the shuffled list to its target position in the original list
2. **Find LIS**: Find the longest increasing subsequence of these positions
   - Elements in the LIS are already in the correct relative order
   - These elements don't need to be moved
3. **Count groups**: Count contiguous groups of elements not in the LIS
   - Each group represents elements that need to be moved
   - Within a group, check if consecutive elements are also consecutive in the original
   - If not consecutive in original, they require separate operations

## Time Complexity

- O(n²) for the LIS calculation using dynamic programming
- O(n) for counting groups
- Overall: O(n²)

## Examples

### Example 1
```
Shuffled: [Whisk, Bake, Season, Fold flour, Fold lettuce]
Original: [Fold flour, Whisk, Bake, Fold lettuce, Season]
Positions: [1, 2, 4, 0, 3]
LIS: [1, 2, 4] (Whisk, Bake, Season)
Non-LIS: Fold flour (pos 0), Fold lettuce (pos 3)
Result: 2 operations (they're not consecutive in original)
```

### Example 2
```
Shuffled: [Dice onion, Dice rice, Pour, Stir, Fold, Serve]
Original: [Pour, Stir, Fold, Dice onion, Dice rice, Serve]
Positions: [3, 4, 0, 1, 2, 5]
LIS: [0, 1, 2, 5] (Pour, Stir, Fold, Serve)
Non-LIS: Dice onion (pos 3), Dice rice (pos 4)
Result: 1 operation (they're consecutive in original: 3→4)
```

## Usage

```bash
python3 solution.py < input.txt
```
