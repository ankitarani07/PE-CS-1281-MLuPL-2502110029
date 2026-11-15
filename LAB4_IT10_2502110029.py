# Taking tests 1-6 as specified
log_lines = hostile[:6] 

valid_diameters = []
rejects = []

for line in log_lines:
    try:
        parts = line.split()
        dia = float(parts[1])
        shift = parts[2] # Accessing 3rd element ensures we have enough fields
        valid_diameters.append(dia)
        
    except AttributeError as e:
        rejects.append((line, "AttributeError: Input lacks string methods (.split)"))
    except IndexError as e:
        rejects.append((line, "IndexError: Missing required fields in log line"))
    except ValueError as e:
        rejects.append((line, "ValueError: Diameter cannot be converted to a float"))

# Guarded average: prevents ZeroDivisionError if all parts are rejected
if len(valid_diameters) > 0:
    guarded_avg = sum(valid_diameters) / len(valid_diameters)
else:
    guarded_avg = 0.0

print("--- Shift Report ---")
print(f"Valid Parts: {len(valid_diameters)}")
print(f"Average Diameter: {guarded_avg:.2f}")

print("\n--- Rejects Table ---")
for bad_line, reason in rejects:
    # Safely print lines that might be empty or whitespace
    display_line = bad_line if str(bad_line).strip() else "[Empty/Whitespace]"
    print(f"Line: {display_line:<20} | Reason: {reason}")
