import random

accept_count = 0
rework_count = 0
scrap_count = 0

# Loop set to 100 as instructed
for i in range(100):
    # Expanded the random range slightly so SCRAP is possible
    diameter = round(random.uniform(24.85, 25.15), 2)
    
    # Placeholder Job 09 bounds
    if 24.95 <= diameter <= 25.05:
        print(f"{diameter} - ACCEPT")
        accept_count += 1
    elif 24.90 <= diameter < 24.95 or 25.05 < diameter <= 25.10:
        print(f"{diameter} - REWORK")
        rework_count += 1
    else:
        print(f"{diameter} - SCRAP")
        scrap_count += 1

print(f"\n--- Shift Report ---")
print(f"ACCEPT: {accept_count} | REWORK: {rework_count} | SCRAP: {scrap_count}")
print("\nRecord: Same code, ten times the work, zero extra effort.")
