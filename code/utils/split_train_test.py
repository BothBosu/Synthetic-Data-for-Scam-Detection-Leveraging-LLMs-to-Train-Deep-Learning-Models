import pandas as pd
from sklearn.model_selection import train_test_split

# Read the CSV file
data = pd.read_csv('../data/single-agent-scam-dialogue_all.csv')

# Get the unique types from the 'type' column
types = data['type'].unique()

# Initialize empty DataFrames for train and test data
train_data = pd.DataFrame()
test_data = pd.DataFrame()

# Iterate over each unique type
for type_value in types:
    # Filter the data for the current type
    type_data = data[data['type'] == type_value]
    
    # Split the data into train and test sets for the current type
    train_type, test_type = train_test_split(type_data, test_size=0.2, random_state=42)
    
    # Append the train and test data for the current type to the respective DataFrames
    train_data = train_data._append(train_type, ignore_index=True)
    test_data = test_data._append(test_type, ignore_index=True)

# Save the train and test data to separate CSV files
train_data.to_csv('../data/single-agent-scam-dialogue_train.csv', index=False)
test_data.to_csv('../data/single-agent-scam-dialogue_test.csv', index=False)