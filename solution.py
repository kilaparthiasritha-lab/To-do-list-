def min_rearrange_cost(n, shuffled, original):
    # Create a mapping of instruction to its position in the original list
    original_pos = {instruction: i for i, instruction in enumerate(original)}
    
    # Map shuffled instructions to their target positions
    shuffled_positions = [original_pos[instruction] for instruction in shuffled]
    
    # Find the longest increasing subsequence (LIS)
    # Elements in LIS don't need to be moved
    
    if n == 0:
        return 0
    
    # dp[i] = length of longest increasing subsequence ending at index i
    dp = [1] * n
    parent = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if shuffled_positions[j] < shuffled_positions[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
    
    # Find the ending index of LIS with maximum length
    lis_length = max(dp)
    lis_end = dp.index(lis_length)
    
    # Reconstruct the LIS
    lis_indices = []
    current = lis_end
    while current != -1:
        lis_indices.append(current)
        current = parent[current]
    lis_indices.reverse()
    
    lis_set = set(lis_indices)
    
    # Count contiguous groups of elements not in LIS
    # BUT: elements can only be moved together if they are:
    # 1. Consecutive in shuffled list
    # 2. Consecutive in original list (their target positions differ by 1)
    
    groups = 0
    i = 0
    while i < n:
        if i not in lis_set:
            # Start of a new group
            groups += 1
            # Extend the group as long as elements are consecutive in both lists
            j = i
            while j < n and j not in lis_set:
                if j + 1 < n and j + 1 not in lis_set:
                    # Check if j and j+1 are consecutive in original
                    if abs(shuffled_positions[j] - shuffled_positions[j + 1]) != 1:
                        # Not consecutive in original, so they need separate operations
                        groups += 1
                j += 1
            i = j
        else:
            i += 1
    
    return groups


# Read input
n = int(input())
input()  # Read "shuffled"

shuffled = []
for _ in range(n):
    shuffled.append(input())

input()  # Read "original"

original = []
for _ in range(n):
    original.append(input())

# Calculate and print result
result = min_rearrange_cost(n, shuffled, original)
print(result)
