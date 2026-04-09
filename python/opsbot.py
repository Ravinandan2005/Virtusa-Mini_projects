import os
from datetime import datetime

log_file = "ensora.log"

# counters
counts = {
    "ERROR": 0,
    "CRITICAL": 0,
    "FAILED LOGIN": 0
}

filtered_logs = []

# read file
with open(log_file, "r") as file:
    for line in file:
        line = line.strip()
        # check conditions - each keyword checked independently
        is_alert = False
        
        if "CRITICAL" in line:
            counts["CRITICAL"] += 1
            is_alert = True

        if "ERROR" in line:
            counts["ERROR"] += 1
            is_alert = True

        if "FAILED LOGIN" in line:
            counts["FAILED LOGIN"] += 1
            is_alert = True
        
        # add to output if any security alert keyword found
        if is_alert:
            filtered_logs.append(line)

# create output file name
date_str = datetime.now().strftime("%d-%m-%Y")
output_file = f"output/security_alert_{date_str}.txt"

# write filtered logs
with open(output_file, "w") as file:
    for log in filtered_logs:
        file.write(log + "\n")

# print summary
print("\n--- Security Alert Summary ---")
print(f"ERROR count: {counts['ERROR']}")
print(f"CRITICAL count: {counts['CRITICAL']}")
print(f"FAILED LOGIN count: {counts['FAILED LOGIN']}")

# file size check
file_size = os.path.getsize(output_file)
print(f"\nOutput file created: {output_file}")
print(f"File size: {file_size} bytes")


#Completed by: J N Ravinandan
#SRM University(Vadapalani)