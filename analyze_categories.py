import csv
import signal
import sys

# Ignore broken pipe errors
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# Dictionary to store colleges and their categories
colleges = {}

# Read the CSV file
with open('josaa2024.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        college = row[0]
        category = row[3]
        
        if college not in colleges:
            colleges[college] = set()
        
        colleges[college].add(category)

# Standard categories
standard_categories = {
    "OPEN", "OBC-NCL", "EWS", "SC", "ST",
    "OPEN-PWD", "OBC-PWD", "EWS-PWD", "SC-PWD", "ST-PWD"
}

# Colleges of interest
colleges_of_interest = [
    "Punjab Engineering College Chandigarh",
    "Indian Institute of Information Technology (IIIT)Kota Rajasthan",
    # Add more colleges here if needed
]

# Print categories for colleges of interest
print("Categories for specific colleges:")
for college_name in colleges_of_interest:
    for college, categories in colleges.items():
        if college_name in college:
            print(f"{college}:")
            print(f"Available: {sorted(list(categories))}")
            print(f"Missing: {sorted(list(standard_categories - categories))}")
            print("-" * 80)

# Count colleges with non-standard category sets
non_standard_count = 0
for college, categories in colleges.items():
    if categories != standard_categories:
        non_standard_count += 1

print(f"\nTotal colleges with non-standard category sets: {non_standard_count} out of {len(colleges)}")

# Find colleges missing OBC-NCL
print("\nColleges missing OBC-NCL category:")
for college, categories in colleges.items():
    if "OBC-NCL" not in categories:
        print(f"- {college}")

# Find colleges missing EWS
print("\nColleges missing EWS category:")
for college, categories in colleges.items():
    if "EWS" not in categories:
        print(f"- {college}") 