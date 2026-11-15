log_lines = [
    "  X-001  25.01   Day",
    "X-002    24.95 Day  ",
    " X-003 25.10   Day",
    "X-004  25.00 Day",
    "  X-005 24.80   Day",
    "X-006 25.05 Day",
    "X-007   25.01 Day",
    "  X-008 24.99   Day",
    "X-009 25.15 Day ",
    " X-010  25.02 Day"
]

diameters = []
for line in log_lines:
    parts = line.split()
    diameters.append(float(parts[1]))

count = len(diameters)
average = sum(diameters) / count
min_dia = min(diameters)
max_dia = max(diameters)

print(f"Count: {count}")
print(f"Average: {average:.2f}")
print(f"Min: {min_dia}")
print(f"Max: {max_dia}")

# Record Justification:
# A list is required instead of a set because multiple parts can have the exact same diameter. 
# A set inherently removes duplicates, which would artificially lower the part count and corrupt the average calculations.
