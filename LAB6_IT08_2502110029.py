# (Assume inspect function is available)

raw_logs = ["X-001 25.01", "X-002 24.80", "X-003 24.98", "X-004 25.20"]

# 1. Build the dictionary from parsed logs
catalogue = {}
for line in raw_logs:
    parts = line.split()
    catalogue[parts[0]] = float(parts[1])

# 2. Lookup tool
def lookup(catalog_dict, code):
    # Uses .get() to return a sensible default instead of crashing on a KeyError
    return catalog_dict.get(code, "ERROR: Part code not found")

# 3. Scrap code extractor
def scrap_codes(catalog_dict):
    # Returns a set of part codes that evaluate to SCRAP
    scrapped = set()
    for code, dia in catalog_dict.items():
        if inspect(dia) == "SCRAP":
            scrapped.add(code)
    return scrapped

# --- Tests ---
print(f"Valid Lookup (X-001): {lookup(catalogue, 'X-001')}")
print(f"Invalid Lookup (Z-999): {lookup(catalogue, 'Z-999')}")
print(f"Scrapped Part Codes: {scrap_codes(catalogue)}")
