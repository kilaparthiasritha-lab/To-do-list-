shuffled = ["Whisk the onion", "Bake the butter", "Season the garlic", "Fold the flour", "Fold the lettuce"]
original = ["Fold the flour", "Whisk the onion", "Bake the butter", "Fold the lettuce", "Season the garlic"]

n = 5

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

# Find ALL possible LIS with maximum length
lis_length = max(dp)
print("LIS length:", lis_length)

# Try all possible LIS endings
all_lis = []
for lis_end in range(n):
    if dp[lis_end] == lis_length:
        # Reconstruct this LIS
        lis_indices = []
        current = lis_end
        while current != -1:
            lis_indices.append(current)
            current = parent[current]
        lis_indices.reverse()
        all_lis.append(lis_indices)
        print(f"LIS ending at {lis_end}: {lis_indices} -> {[shuffled[i] for i in lis_indices]}")

# Try each LIS and count groups
for lis_indices in all_lis:
    lis_set = set(lis_indices)
    groups = 0
    in_group = False
    
    for i in range(n):
        if i not in lis_set:
            if not in_group:
                groups += 1
                in_group = True
        else:
            in_group = False
    
    print(f"  Groups for this LIS: {groups}")
