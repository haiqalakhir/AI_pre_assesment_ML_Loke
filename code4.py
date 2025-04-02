# Import the pandas library
import pandas as pd

# Define valid statuses globally
VALID_STATUSES = ["OK", "FAULTY", "MAINTENANCE", "INACTIVE"]

# Function to read the file and return the lines
def read_file(filename):
    with open(filename, "r") as file:
        return file.readlines()

# Function to clean and process a line of statuses
def process_line(line):
    # Split the line by commas
    raw_statuses = line.split(",")
    # Clean and normalize each status (strip spaces, make uppercase)
    cleaned_statuses = [status.strip().upper() for status in raw_statuses]
    return cleaned_statuses

# Function to count valid and invalid statuses
def count_statuses(lines):
    valid_counts = {status: 0 for status in VALID_STATUSES}  # Initialize counts for valid statuses
    invalid_count = 0  # Counter for invalid statuses
    
    for line in lines:
        statuses = process_line(line)
        for status in statuses:
            if status in VALID_STATUSES:
                valid_counts[status] += 1
            elif status:  # Count invalid statuses (ignore empty ones)
                invalid_count += 1
    
    return valid_counts, invalid_count

# Function to display the results
def display_results(valid_counts, invalid_count):
    # Convert the counts into a pandas DataFrame for easier sorting
    df = pd.DataFrame(valid_counts.items(), columns=["Status", "Count"])
    
    # Sort and display by status name (A-Z)
    sorted_by_name = df.sort_values("Status")
    print("Status Counts (Sorted by Name):")
    print(sorted_by_name)
    
    # Sort and display by count (descending)
    sorted_by_count = df.sort_values("Count", ascending=False)
    print("\nStatus Counts (Sorted by Count):")
    print(sorted_by_count)
    
    # Display the number of invalid statuses
    print(f"\nInvalid statuses skipped: {invalid_count}")

# Main function to execute the script
def main():
    filename = "machines_txt.txt"  # Replace with your file name
    lines = read_file(filename)  # Step 1: Read the file
    valid_counts, invalid_count = count_statuses(lines)  # Step 2: Process lines and count statuses
    display_results(valid_counts, invalid_count)  # Step 3: Display the results

# Run the main function
if __name__ == "__main__":
    main()
