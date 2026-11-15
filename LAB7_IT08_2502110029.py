import random

# Using the GuardedMachine class from IT10
bench_mill = GuardedMachine("Mill-Delta", 4000)

print("--- Starting Shift ---")
for i in range(10):
    # Simulate receiving jobs with random RPM requirements (some will intentionally fail)
    job_rpm = random.randint(3500, 4500) 
    
    # The machine handles its own counters and validation internally
    bench_mill.process_part(job_rpm)

print("\n--- Shift Report ---")
print(bench_mill.status())
