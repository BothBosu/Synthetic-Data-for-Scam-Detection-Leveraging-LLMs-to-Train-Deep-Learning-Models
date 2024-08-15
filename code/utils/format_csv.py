
import csv
import re

def clean_conversation(text):
    # Remove content inside parentheses
    text = re.sub(r'\([^)]*\)', '', text)
    
    # Replace "caller" with "Suspect" and "receiver" with "Innocent"
    text = text.replace("caller", "Suspect").replace("receiver", "Innocent")
    
    # Remove text before the first occurrence of "Suspect:"
    match = re.search(r'\bSuspect:', text)
    if match:
        return text[match.start():]
    else:
        return text

# Specify the paths to your input and output CSV files
input_csv_path = ""
output_csv_path = ""

# Open the input CSV file in read mode and the output CSV file in write mode
with open(input_csv_path, "r", newline='', encoding='utf-8-sig') as infile, \
     open(output_csv_path, "w", newline='', encoding='utf-8') as outfile:
    
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    # Iterate over each row in the input CSV file
    for row in reader:
        if 'dialogue' in row:
            # Clean the dialogue text
            row['dialogue'] = clean_conversation(row['dialogue'])
        
        # Write the updated row to the output file
        writer.writerow(row)

print(f"CSV file has been processed. Updated content saved to {output_csv_path}")