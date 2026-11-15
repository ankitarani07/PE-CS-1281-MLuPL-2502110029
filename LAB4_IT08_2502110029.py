import random

mode = input("Enter operator mode (halt/skip): ").strip().lower()
inspected_count = 0
scrap_count = 0

for i in range(100):
    diameter = round(random.uniform(24.85, 25.15), 2)
    inspected_count += 1
    
    if 24.95 <= diameter <= 25.05:
        pass # ACCEPT
    elif 24.90 <= diameter < 24.95 or 25.05 < diameter <= 25.10:
        pass # REWORK
    else:
        # SCRAP condition met
        if mode == "halt":
            print(f"SCRAP found ({diameter}). Halting production.")
            break
        elif mode == "skip":
            print(f"SCRAP logged ({diameter}). Skipping.")
            scrap_count += 1
            continue

if mode == "halt":
    print(f"Parts inspected before stop: {inspected_count}")
else:
    print(f"Batch finished. Total scrap skipped: {scrap_count}")
