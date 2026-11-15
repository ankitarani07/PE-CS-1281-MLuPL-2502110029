log_lines = [
    "X-001 25.01 Day", "X-002 24.95 Day", "X-003 25.10 Day", 
    "X-004 25.00 Day", "X-005 24.80 Day", "X-006 25.05 Day"
]

accepted_diameters = []
rework_diameters = []
scrap_diameters = []
scrapped_part_codes = []

for line in log_lines:
    parts = line.split()
    code = parts[0]
    dia = float(parts[1])
    
    # Placeholder sorting logic
    if 24.95 <= dia <= 25.05:
        accepted_diameters.append(dia)
    elif 24.90 <= dia < 24.95 or 25.05 < dia <= 25.10:
        rework_diameters.append(dia)
    else:
        scrap_diameters.append(dia)
        scrapped_part_codes.append(code)

if len(accepted_diameters) > 0:
    accepted_avg = sum(accepted_diameters) / len(accepted_diameters)
else:
    accepted_avg = 0

print(f"ACCEPTED count: {len(accepted_diameters)}")
print(f"REWORK count: {len(rework_diameters)}")
print(f"SCRAP count: {len(scrap_diameters)}")
print(f"Accepted Average: {accepted_avg:.2f}")
print(f"Scrapped Part Codes: {scrapped_part_codes}")
