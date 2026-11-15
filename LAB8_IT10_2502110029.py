
# A list of 8 hostile inputs representing corrupted or malformed data
hostile = [
    "X-001 twenty Day",  # 1. String where a float is expected
    "X-002",             # 2. Missing fields
    "",                  # 3. Empty string
    "X-004 25.01",       # 4. Missing the shift field
    "   ",               # 5. Whitespace only
    "X-006 25.0.1 Day",  # 6. Malformed float (two decimal points)
    None,                # 7. NoneType object instead of string
    []                   # 8. List object instead of string
]

# Record for your lab: 
# If run against a basic Lab 05 parser (e.g., `float(line.split()[1])`), 
# test 1 ("X-001 twenty Day") kills the program immediately with a ValueError.
