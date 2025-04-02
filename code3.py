# Import the pandas library
import pandas as pd

# Step 1: Define the valid statuses
# These are the statuses we want to count: OK, FAULTY, MAINTENANCE, INACTIVE
valid_statuses = ["OK", "FAULTY", "MAINTENANCE", "INACTIVE"]

# Step 2: Provide the file name
# Replace "machines_txt.txt" with your actual file name if it's different
filename = "machines_txt.txt"

# Step 3: Open the file and read the lines
# This reads all the lines of the file into a list called 'lines'
with open(filename, "r") as file:
    lines = file.readlines()

# Step 4: Create a dictionary to store the count of each valid status
# We start all counts at 0
status_counts = {
    "OK": 0,
    "FAULTY": 0,
    "MAINTENANCE": 0,
    "INACTIVE": 0
}

# Step 5: Create a variable to count invalid statuses
# This keeps track of how many invalid entries we skipped
invalid_count = 0

# Step 6: Process each line of the file
for line in lines:
    # Split the line into individual statuses by commas
    # For example, "ok, faulty" becomes ["ok", "faulty"]
    raw_statuses = line.split(",")

    # Step 7: Normalize each status (remove extra spaces and make uppercase)
    normalized_statuses = []
    for raw_status in raw_statuses:
        normalized_status = raw_status.strip().upper()
        normalized_statuses.append(normalized_status)

    # Step 8: Count valid and invalid statuses
    for normalized_status in normalized_statuses:
        if normalized_status in valid_statuses:
            # If the status is valid, add 1 to its count
            status_counts[normalized_status] += 1
        elif normalized_status != "":
            # If the status is not valid and not empty, increase invalid count
            invalid_count += 1

# Step 9: Display the counts sorted by name (A-Z)
print("Status Counts (Sorted by Name):")
for status in sorted(status_counts.keys()):
    print(f"{status}: {status_counts[status]}")

# Step 10: Display the counts sorted by count (descending)
print("\nStatus Counts (Sorted by Count):")
sorted_status_counts = sorted(status_counts.items(), key=lambda x: x[1], reverse=True)
for status, count in sorted_status_counts:
    print(f"{status}: {count}")

# Step 11: Display the number of invalid statuses skipped
print(f"\nInvalid statuses skipped: {invalid_count}")
