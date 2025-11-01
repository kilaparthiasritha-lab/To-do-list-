def verify_example(shuffled, original, expected):
    n = len(shuffled)
    original_pos = {instruction: i for i, instruction in enumerate(original)}
    shuffled_positions = [original_pos[instruction] for instruction in shuffled]
    
    print(f"Shuffled: {shuffled}")
    print(f"Original: {original}")
    print(f"Positions: {shuffled_positions}")
    
    # Find LIS
    dp = [1] * n
    parent = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if shuffled_positions[j] < shuffled_positions[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
    
    lis_length = max(dp)
    lis_end = dp.index(lis_length)
    
    lis_indices = []
    current = lis_end
    while current != -1:
        lis_indices.append(current)
        current = parent[current]
    lis_indices.reverse()
    
    lis_set = set(lis_indices)
    print(f"LIS indices: {lis_indices}")
    print(f"LIS elements: {[shuffled[i] for i in lis_indices]}")
    
    # Count groups
    groups = 0
    i = 0
    while i < n:
        if i not in lis_set:
            groups += 1
            print(f"Group {groups} starts at index {i}: {shuffled[i]}")
            j = i
            while j < n and j not in lis_set:
                if j + 1 < n and j + 1 not in lis_set:
                    if abs(shuffled_positions[j] - shuffled_positions[j + 1]) != 1:
                        groups += 1
                        print(f"  -> Not consecutive in original, new group {groups} at index {j+1}: {shuffled[j+1]}")
                j += 1
            i = j
        else:
            i += 1
    
    print(f"Result: {groups}, Expected: {expected}")
    print(f"{'✓ PASS' if groups == expected else '✗ FAIL'}")
    print()

# Example 1
shuffled1 = ["Whisk the onion", "Bake the butter", "Season the garlic", "Fold the flour", "Fold the lettuce"]
original1 = ["Fold the flour", "Whisk the onion", "Bake the butter", "Fold the lettuce", "Season the garlic"]
verify_example(shuffled1, original1, 2)

# Example 2
shuffled2 = ["Dice the onion", "Dice the rice", "Pour the onion", "Stir the egg", "Fold the lettuce", "Serve the tomato"]
original2 = ["Pour the onion", "Stir the egg", "Fold the lettuce", "Dice the onion", "Dice the rice", "Serve the tomato"]
verify_example(shuffled2, original2, 1)
