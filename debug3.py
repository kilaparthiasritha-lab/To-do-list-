shuffled = ["Dice the onion", "Dice the rice", "Pour the onion", "Stir the egg", "Fold the lettuce", "Serve the tomato"]
original = ["Pour the onion", "Stir the egg", "Fold the lettuce", "Dice the onion", "Dice the rice", "Serve the tomato"]

n = 6

# Create a mapping of instruction to its position in the original list
original_pos = {instruction: i for i, instruction in enumerate(original)}

# Map shuffled instructions to their target positions
shuffled_positions = [original_pos[instruction] for instruction in shuffled]

print("Shuffled positions in original:", shuffled_positions)

# dp[i] = length of longest increasing subsequence ending at index i
dp = [1] * n
parent = [-1] * n

for i in range(1, n):
    for j in range(i):
        if shuffled_positions[j] < shuffled_positions[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

print("DP:", dp)

# Find the ending index of LIS with maximum length
lis_length = max(dp)
lis_end = dp.index(lis_length)

print("LIS length:", lis_length)

# Reconstruct the LIS
lis_indices = []
current = lis_end
while current != -1:
    lis_indices.append(current)
    current = parent[current]
lis_indices.reverse()

print("LIS indices:", lis_indices)
print("LIS elements:", [shuffled[i] for i in lis_indices])

lis_set = set(lis_indices)

# Count contiguous groups of elements not in LIS
groups = 0
in_group = False

for i in range(n):
    if i not in lis_set:
        if not in_group:
            groups += 1
            in_group = True
            print(f"Starting group {groups} at index {i}: {shuffled[i]}")
    else:
        in_group = False
        print(f"Index {i} is in LIS: {shuffled[i]}")

print("Total groups:", groups)
