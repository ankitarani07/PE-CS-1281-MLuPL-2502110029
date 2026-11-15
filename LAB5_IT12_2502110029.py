raw_line = "A-101   25.02   Morning"

# .split() automatically handles multiple spaces and tabs
parts = raw_line.split()

part_code = parts[0]
diameter = float(parts[1])
shift = parts[2]

print(f"Part Code: {part_code}")
print(f"Diameter: {diameter}")
print(f"Shift: {shift}")
print(f"Proof of float: {diameter + 0.01}")
