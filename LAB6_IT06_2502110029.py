# shoptools.py
def inspect(dia):
    if 24.95 <= dia <= 25.05: return "ACCEPT"
    elif 24.90 <= dia < 24.95 or 25.05 < dia <= 25.10: return "REWORK"
    else: return "SCRAP"

def tally(labels):
    counts = {"ACCEPT": 0, "REWORK": 0, "SCRAP": 0}
    for label in labels:
        if label in counts: counts[label] += 1
    return counts

def report(shift, counts):
    return f"[{shift} Shift] ACCEPT: {counts.get('ACCEPT', 0)} | REWORK: {counts.get('REWORK', 0)} | SCRAP: {counts.get('SCRAP', 0)}"

def lookup(catalog_dict, code):
    return catalog_dict.get(code, "Not found")

def scrap_codes(catalog_dict):
    scrapped = set()
    for code, dia in catalog_dict.items():
        if inspect(dia) == "SCRAP":
            scrapped.add(code)
    return scrapped
