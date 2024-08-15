import csv
from collections import defaultdict

def check_duplicate_conversations(csv_file):
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
            csv_reader = csv.DictReader(file)
            print("Columns in the CSV file:", csv_reader.fieldnames)
            
            dialogues = defaultdict(list)
            for row_num, row in enumerate(csv_reader, start=1):
                if 'dialogue' in row:
                    dialogues[row['dialogue']].append(row_num)
                else:
                    print("Error: 'dialogue' column not found in the CSV file.")
                    return
    
        # Filter and count duplicates
        duplicates = {dialogue: rows for dialogue, rows in dialogues.items() if len(rows) > 1}
        
        if duplicates:
            print(f"Number of dialogues with duplicates: {len(duplicates)}")
            print("\nDuplicate dialogues found:")
            for dialogue, rows in duplicates.items():
                print(f"'{dialogue}' appears {len(rows)} times in rows: {', '.join(map(str, rows))}")
        else:
            print("No duplicate dialogues found.")
    
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read the file '{csv_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


csv_file_path = '../data/single-agent-scam-dialogue_all.csv'
# csv_file_path = '../agentGenerator/data/agent_conversation_all.csv'
check_duplicate_conversations(csv_file_path)