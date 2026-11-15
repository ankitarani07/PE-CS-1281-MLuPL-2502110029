def inspect(dia):
    """Returns a bin label based on diameter."""
    if 24.95 <= dia <= 25.05:
        return "ACCEPT"
    elif 24.90 <= dia < 24.95 or 25.05 < dia <= 25.10:
        return "REWORK"
    else:
        return "SCRAP"

def tally(labels):
    """Takes a list of labels and returns a count dictionary."""
    counts = {"ACCEPT": 0, "REWORK": 0, "SCRAP": 0}
    for label in labels:
        if label in counts:
            counts[label] += 1
    return counts

def report(shift, counts):
    """Takes a shift name and counts dict, returns a formatted string."""
    return f"[{shift} Shift] ACCEPT: {counts.get('ACCEPT', 0)} | REWORK: {counts.get('REWORK', 0)} | SCRAP: {counts.get('SCRAP', 0)}"

# --- Independent Tests ---
print("Test inspect:", inspect(25.00))
print("Test tally:", tally(["ACCEPT", "REWORK", "ACCEPT", "SCRAP", "SCRAP"]))
print("Test report:", report("Morning", {"ACCEPT": 50, "REWORK": 12, "SCRAP": 3}))
