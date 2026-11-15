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
