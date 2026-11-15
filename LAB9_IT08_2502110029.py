import re

# Regex pattern tolerates any spacing (\s*), requires a shape like X-123, a float, and a shift word
pattern = re.compile(r"^\s*([A-Z]-\d{3})\s+(\d+\.\d+)\s+([A-Za-z]+)\s*$")

def parse_regex(line):
    match = pattern.match(line)
    if match:
        return match.group(1), float(match.group(2)), match.group(3)
    else:
        raise ValueError("Format mismatch: Line rejected by regex pattern")

# --- RECORD NOTE REQUIRED BY ASSIGNMENT ---
# def parse_split(line):
#     parts = line.split()
#     return parts[0], float(parts[1]), parts[2]
# 
# Which one survived more test lines? 
# Answer: The regex version survives more test lines gracefully. `.split()` blindly attempts 
# to cast data and throws IndexErrors/ValueErrors deep inside the logic. Regex natively validates 
# the part code shape and the presence of a float upfront, acting as a much stronger gatekeeper.
