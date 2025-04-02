file_path = "machines_txt.txt"  # Path to your uploaded file
valid_statuses = ["OK", "FAULTY", "MAINTENANCE", "INACTIVE"]
status_counts = {status: 0 for status in valid_statuses}
invalid_count = 0

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        if not line:  # Skip empty lines
            continue

        statuses = [status.strip().upper() for status in line.split(",")]
        for status in statuses:
            if status in valid_statuses:
                status_counts[status] += 1
            else:
                invalid_count += 1

# Display results (sorted by name)
print("Status Counts (Sorted by Name):")
for status in sorted(status_counts.keys()):
    print(f"{status}: {status_counts[status]}")
print(f"Invalid statuses skipped: {invalid_count}")

# Display results (sorted by count - descending)
print("\nStatus Counts (Sorted by Count):")
sorted_items = sorted(status_counts.items(), key=lambda item: item[1], reverse=True)
for status, count in sorted_items:
    print(f"{status}: {count}")
