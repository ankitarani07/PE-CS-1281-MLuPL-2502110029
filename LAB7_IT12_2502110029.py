class CNCMachine:
    def __init__(self, model_name, max_rpm):
        # Three attributes, including one limit (max_rpm)
        self.model_name = model_name
        self.max_rpm = max_rpm
        self.parts_produced = 0

    def __str__(self):
        # Nameplate
        return f"[{self.model_name}] Rated for max {self.max_rpm} RPM"

    def process_part(self):
        # Working method
        self.parts_produced += 1

# Commission two machines
lathe = CNCMachine("Lathe-Alpha", 3000)
mill = CNCMachine("Mill-Beta", 4500)

# Prove their states are independent
lathe.process_part()
lathe.process_part()
mill.process_part()

print(lathe)
print(f"Lathe production: {lathe.parts_produced}")
print(mill)
print(f"Mill production: {mill.parts_produced}")
