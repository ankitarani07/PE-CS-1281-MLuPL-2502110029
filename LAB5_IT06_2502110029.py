day_shift_logs = [
    "D-001 25.00 Day", "D-002 24.80 Day", "D-003 24.98 Day", "D-004 25.20 Day"
]
night_shift_logs = [
    "N-001 25.01 Night", "D-002 24.75 Night", "N-003 25.05 Night", "D-004 24.60 Night"
]

def parse_shift(logs):
    accepts = 0
    scrap_codes = set()
    for line in logs:
        parts = line.split()
        code = parts[0]
        dia = float(parts[1])
        
        # Placeholder logic
        if 24.95 <= dia <= 25.05:
            accepts += 1
        elif dia < 24.90 or dia > 25.10:
            scrap_codes.add(code)
            
    accept_rate = (accepts / len(logs)) * 100 if logs else 0
    return accept_rate, scrap_codes

day_rate, day_scraps = parse_shift(day_shift_logs)
night_rate, night_scraps = parse_shift(night_shift_logs)

print(f"Day Shift Accept Rate: {day_rate:.1f}%")
print(f"Night Shift Accept Rate: {night_rate:.1f}%")

# Using Set operations
both_shifts_scrap = day_scraps.intersection(night_scraps)
unique_to_one_scrap = day_scraps.symmetric_difference(night_scraps)

print(f"Codes scrapped in BOTH shifts (Intersection): {both_shifts_scrap}")
print(f"Codes scrapped in ONLY ONE shift (Symmetric Difference): {unique_to_one_scrap}")
