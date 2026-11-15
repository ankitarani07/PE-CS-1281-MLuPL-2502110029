total_parts = int(input("Enter total parts: "))
box_size = int(input("Enter box size: "))

# Calculate full boxes and loose parts
full_boxes = total_parts // box_size
loose_parts = total_parts % box_size

print(f"Full boxes: {full_boxes}")
print(f"Loose parts: {loose_parts}")

# Print the audit line showing True
audit_check = (full_boxes * box_size) + loose_parts == total_parts
print(f"Audit (boxes*size + loose == total): {audit_check}")
