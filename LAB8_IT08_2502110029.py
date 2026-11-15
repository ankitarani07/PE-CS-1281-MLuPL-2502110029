# 1. Define the custom domain exception
class SpecViolation(Exception):
    """Raised when a machine receives an out-of-bounds command."""
    pass

# 2. Update the Machine class from previous labs
class GuardedMachine:
    def __init__(self, name, max_rpm):
        self.name = name
        self.max_rpm = max_rpm
        self.parts_produced = 0

    def process(self, rpm_command):
        if rpm_command <= 0 or rpm_command > self.max_rpm:
            # Raise the exception instead of just printing an error
            raise SpecViolation(f"Command {rpm_command} RPM exceeds limit of {self.max_rpm}.")
        
        self.parts_produced += 1
        return True

# 3. Driving program catching the exception
mill = GuardedMachine("Mill-Alpha", 4000)
batch_jobs = [3500, 4500, 3800] # 4500 RPM will trigger the SpecViolation

print("--- Starting Batch ---")
for job in batch_jobs:
    try:
        mill.process(job)
        print(f"Success: Processed job at {job} RPM")
    except SpecViolation as error:
        # Catching the error ensures one bad job never stops the fleet
        print(f"Job Rejected: {error} - Moving to next job.")

print(f"Total parts produced: {mill.parts_produced}")
