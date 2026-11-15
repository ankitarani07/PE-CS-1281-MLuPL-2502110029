import os

# Create the data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# 12 clean records + 3 filthy ones from Lab 08
records = [
    "X-001 25.01 Day\n", "X-002 24.95 Day\n", "X-003 25.10 Day\n",
    "X-004 25.00 Day\n", "X-005 24.80 Day\n", "X-006 25.05 Day\n",
    "X-007 25.01 Day\n", "X-008 24.99 Day\n", "X-009 25.15 Day\n",
    "X-010 25.02 Day\n", "X-011 25.00 Day\n", "X-012 24.98 Day\n",
    "X-013 twenty Day\n",  # Filthy 1: Bad float
    "X-014\n",             # Filthy 2: Missing fields
    "   \n"                # Filthy 3: Whitespace only
]

# Write to file
with open("data/shift_log.txt", "w") as f:
    f.writelines(records)

# Read back and print the line count
with open("data/shift_log.txt", "r") as f:
    lines = f.readlines()
    print(f"Line count read from file: {len(lines)}")
