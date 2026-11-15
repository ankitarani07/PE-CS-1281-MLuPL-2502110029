IT12: Rough cut · Fix Yesterday's GapsInstead of scattering try/except blocks everywhere to hide tracebacks, you can override Python's global exception handler to intercept all crashes and print a clean, industrial-style message. For relative paths, abandon os.path and use the modern, object-oriented pathlib.   Pythonimport sys
from pathlib import Path

# 1. Uncommon Relative Paths: Dynamically find the project root based on this file's location
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"

# 2. Uncommon Traceback Suppression: Override the global exception hook
def shop_floor_error_handler(exc_type, exc_value, exc_traceback):
    # This prevents the ugly traceback and prints a clean, user-friendly message
    print(f"\n[SYSTEM HALT] A critical fault occurred: {exc_type.__name__} - {exc_value}")
    print("Please check the input data and try again.")

sys.excepthook = shop_floor_error_handler

# 3. Targeted Exception Handling (Removing bare excepts)
try:
    with open(DATA_DIR / "shift_log.txt", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    # Specifically catching the exact species of error
    print(f"Missing File: {e.filename} could not be located in the data directory.")
