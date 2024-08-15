import pandas as pd
from sklearn.model_selection import train_test_split

# Function to split the data for each type and personality
def split_data(data):
    train_data = pd.DataFrame()
    test_data = pd.DataFrame()
    
    # Group by type and personality
    grouped = data.groupby(['type', 'personality'])
    
    for (type_name, personality_name), group in grouped:
        # Split the group
        train, test = train_test_split(group, test_size=0.2, random_state=42)
        
        # Concatenate to the respective dataframes
        train_data = pd.concat([train_data, train])
        test_data = pd.concat([test_data, test])
    
    return train_data, test_data

# Read the data
file_path = 'agentGenerator/data/llama3_agent_1600.csv'
data = pd.read_csv(file_path)

# Split the data
train_data, test_data = split_data(data)

# Save the splits to CSV files
train_data.to_csv('agentGenerator/data/llama3_agent_train_1200.csv', index=False)
test_data.to_csv('agentGenerator/data/llama3_agent_test_400.csv', index=False)
