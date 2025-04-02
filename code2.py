import pandas as pd

# Define valid statuses and file name
valid_statuses = {"OK", "FAULTY", "MAINTENANCE", "INACTIVE"}
filename = "machines_txt.txt"

# Read the file and process each line
with open(filename, "r") as file:
    lines = file.readlines()

# Initialize counts and invalid count
status_counts = {status: 0 for status in valid_statuses}
invalid_count = 0

for line in lines:
    # Split by commas, normalize cases, and strip whitespace
    statuses = [status.strip().upper() for status in line.split(",")]
    
    for status in statuses:
        if status in valid_statuses:
            status_counts[status] += 1
        elif status:  # Count as invalid if not empty
            invalid_count += 1

# Convert to DataFrame for sorting
df = pd.DataFrame(list(status_counts.items()), columns=["Status", "Count"])

# Sort by name (A-Z)
sorted_by_name = df.sort_values("Status")
print("Status Counts (Sorted by Name):")
print(sorted_by_name)

# Sort by count (descending)
sorted_by_count = df.sort_values("Count", ascending=False)
print("\nStatus Counts (Sorted by Count):")
print(sorted_by_count)

# Display invalid status count
print(f"\nInvalid statuses skipped: {invalid_count}")
