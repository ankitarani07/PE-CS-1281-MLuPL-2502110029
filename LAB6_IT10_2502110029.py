import random

# (Assume inspect, tally, and report functions are defined here)

# Generating sample data to simulate the bench
diameters = [round(random.uniform(24.85, 25.15), 2) for _ in range(100)]

# --- Refactored Main Logic ---
bin_labels = [inspect(dia) for dia in diameters]
final_counts = tally(bin_labels)
print(report("Day", final_counts))

# Record for your submission:
# Before refactor: ~20-25 lines of nested loops and if/elif statements.
# After refactor: Main execution logic is now just 3 lines of clean, readable steps. Output remains identical.
