import os
import glob
import datetime
import re

pattern = re.compile(r"^\s*([A-Z]-\d{3})\s+(\d+\.\d+)\s+([A-Za-z]+)\s*$")
plant_total_valid = 0

# Ensure the run history file has a header if it's new
history_file = "data/run_history.csv"
if not os.path.exists(history_file):
    with open(history_file, "w") as f:
        f.write("Timestamp,File Name,Records Processed,Rejects\n")

# Loop over every .txt file in data/ (matching *_log.txt to ignore reports)
log_files = glob.glob("data/*_log.txt")

for file_path in log_files:
    file_name = os.path.basename(file_path)
    valid_count = 0
    reject_count = 0
    
    with open(file_path, "r") as f:
        for line in f:
            if not line.strip(): continue # Skip blank lines in batch
            
            if pattern.match(line):
                valid_count += 1
                plant_total_valid += 1
            else:
                reject_count += 1
                
    total_processed = valid_count + reject_count
    
    # Append a one-line entry per run to data/run_history.csv
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(history_file, "a") as f:
        f.write(f"{timestamp},{file_name},{total_processed},{reject_count}\n")

print(f"Batch Processing Complete. Combined Plant Total Valid: {plant_total_valid}")
