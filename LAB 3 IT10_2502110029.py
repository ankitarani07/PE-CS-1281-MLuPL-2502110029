accept_count = 0
rework_count = 0
scrap_count = 0

for i in range(10):
    diameter = float(input(f"Enter diameter for part {i+1}: "))
    
    # NOTE: Adjust these boundary numbers based on your specific lab rules!
    if 9.8 <= diameter <= 10.2:
        accept_count += 1
    elif 9.5 <= diameter < 9.8 or 10.2 < diameter <= 10.5:
        rework_count += 1
    else:
        scrap_count += 1

print(f"Final Report - ACCEPT: {accept_count}, REWORK: {rework_count}, SCRAP: {scrap_count}")
