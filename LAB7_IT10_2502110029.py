class GuardedMachine:
    def __init__(self, model_name, max_rpm):
        self.model_name = model_name
        self.__max_rpm = max_rpm
        self.__parts_produced = 0  # Private state

    def __str__(self):
        return f"[{self.model_name}]"

    def process_part(self, rpm_command):
        # Validating operating method
        if 0 < rpm_command <= self.__max_rpm:
            self.__parts_produced += 1
            return True
        else:
            print(f"ERROR on {self.model_name}: Command {rpm_command} RPM out of bounds! Max is {self.__max_rpm}.")
            return False

    def status(self):
        # Getter method
        return f"{self.model_name} Shift Status: {self.__parts_produced} parts produced."

# Record for your submission:
# The one line a careless colleague could use to bypass the guard:
# machine_instance._GuardedMachine__parts_produced = 9999
# 
# Why Python allows this: Python relies on convention and the philosophy that "we are all consenting adults here." 
# Name mangling prevents accidental overwriting of variables, but it doesn't strictly forbid intentional overriding if a developer decides they absolutely need to manipulate the internal state.
