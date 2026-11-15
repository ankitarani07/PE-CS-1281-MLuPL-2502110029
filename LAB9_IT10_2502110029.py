valid_records = []
rejects = []

# 1. Read & Parse
with open("data/shift_log.txt", "r") as f:
    for line in f:
        original_line = line.strip()
        if not original_line:
            rejects.append(("[Empty/Whitespace]", "IndexError: Missing required fields"))
            continue
        
        try:
            parts = line.split()
            if len(parts) < 3:
                raise IndexError("Missing required fields")
            
            code = parts[0]
            dia = float(parts[1])
            shift = parts[2]
            valid_records.append((code, dia, shift))
            
        except ValueError:
            rejects.append((original_line, "ValueError: Diameter cannot be converted to float"))
        except IndexError as e:
            rejects.append((original_line, f"IndexError: {e}"))

# 2. Aggregate
avg_dia = sum(r[1] for r in valid_records) / len(valid_records) if valid_records else 0

# 3. Write data/report.txt (aligned columns)
with open("data/report.txt", "w") as f:
    f.write(f"{'Part Code':<15} | {'Diameter':<10} | {'Shift':<10}\n")
    f.write("-" * 45 + "\n")
    for code, dia, shift in valid_records:
        f.write(f"{code:<15} | {dia:<10.2f} | {shift:<10}\n")
    f.write("-" * 45 + "\n")
    f.write(f"Total Valid: {len(valid_records)} | Plant Average: {avg_dia:.2f}\n")

# 4. Write data/rejects.csv
import csv
with open("data/rejects.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Line", "Reason"])
    for line, reason in rejects:
        writer.writerow([line, reason])
