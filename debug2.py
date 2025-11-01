shuffled = ["Dice the onion", "Dice the rice", "Pour the onion", "Stir the egg", "Fold the lettuce", "Serve the tomato"]
original = ["Pour the onion", "Stir the egg", "Fold the lettuce", "Dice the onion", "Dice the rice", "Serve the tomato"]

n = 6

# Create a mapping of instruction to its position in the original list
original_pos = {instruction: i for i, instruction in enumerate(original)}

# Map shuffled instructions to their target positions
shuffled_positions = [original_pos[instruction] for instruction in shuffled]

print("Shuffled:", shuffled)
print("Original:", original)
print("Shuffled positions in original:", shuffled_positions)

# dp[i] = length of longest increasing subsequence ending at index i
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if shuffled_positions[j] < shuffled_positions[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print("DP:", dp)
lis_length = max(dp)
print("LIS length:", lis_length)
print("Answer (n - LIS):", n - lis_length)
print()
print("Expected: 1")
print("Explanation: Move 'Dice the onion' and 'Dice the rice' together (1 operation)")
