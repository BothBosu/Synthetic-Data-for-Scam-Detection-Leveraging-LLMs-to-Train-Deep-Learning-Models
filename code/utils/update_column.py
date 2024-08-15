import os
import csv

# Specify the directory path
directory = ''

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a CSV file
    if filename.endswith('.csv'):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Read the CSV file
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        # Update the column names
        updated_rows = []
        for row in rows:
            updated_row = ['label' if col == 'lable' else col for col in row]
            updated_rows.append(updated_row)
        
        # Write the updated rows back to the CSV file
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        
        print(f"Column names updated in {filename}")