import random

consecutive_accepts = 0
parts_machined = 0
safety_cap = 500

while consecutive_accepts < 5 and parts_machined < safety_cap:
    parts_machined += 1
    diameter = round(random.uniform(24.85, 25.15), 2)
    
    if 24.95 <= diameter <= 25.05:
        consecutive_accepts += 1
        print(f"Part {parts_machined}: {diameter} - ACCEPT ({consecutive_accepts}/5)")
    else:
        consecutive_accepts = 0
        print(f"Part {parts_machined}: {diameter} - REJECTED (Streak reset)")

if consecutive_accepts == 5:
    print(f"\nTarget reached! It took {parts_machined} parts to get 5 consecutive ACCEPTs.")
else:
    print(f"\nSafety cap of {safety_cap} reached. Production stopped.")

print("\nRecord: An industrial program always requires a safety cap to prevent an infinite loop, which could cause hardware lockups, physical tool damage, or uncontrolled material waste if a mechanical error makes a 'good' part physically impossible to produce.")
