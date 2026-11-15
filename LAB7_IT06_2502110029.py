# shoptools.py

class FleetMachine:
    def __init__(self, machine_id, max_rpm):
        self.machine_id = machine_id
        self.__max_rpm = max_rpm
        self.__parts_produced = 0
        self.is_free = True

    def __str__(self):
        return f"[{self.machine_id}]"

    def process_part(self):
        self.__parts_produced += 1
        
    def get_parts_count(self):
        return self.__parts_produced

    def status(self):
        return f"{self.machine_id}: {self.__parts_produced} parts"
        import shoptools
import random

# Initialize a list of three machines
plant_fleet = [
    shoptools.FleetMachine("Machine-1", 3000),
    shoptools.FleetMachine("Machine-2", 4000),
    shoptools.FleetMachine("Machine-3", 3500)
]

# Simulate 50 jobs arriving at the plant
for _ in range(50):
    # Allocate to whichever machine is free 
    # (Simulated here by filtering for 'is_free', though for this simple loop all are always instantly free)
    available_machines = [m for m in plant_fleet if m.is_free]
    
    # Assign the job to a random available machine in the list
    chosen_machine = random.choice(available_machines)
    chosen_machine.process_part()

# --- Plant Report ---
print("--- End of Shift Plant Report ---")
plant_total = 0

for machine in plant_fleet:
    print(machine.status())
    plant_total += machine.get_parts_count()

print(f"\nPlant Total Production: {plant_total} parts")

# Find the busiest machine using max() and a lambda function
busiest_machine = max(plant_fleet, key=lambda m: m.get_parts_count())

print(f"Busiest Machine: {busiest_machine.machine_id} with {busiest_machine.get_parts_count()} parts processed.")

