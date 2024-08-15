import replicate
import streamlit as st
import pandas as pd


# Function for generating LLaMA3 response
temperature = 0.8
top_p = 0.9
max_length = 1024
llm = "meta/meta-llama-3-70b-instruct"
replicate_api = st.secrets['REPLICATE_API_TOKEN']

def generate_llama_response():
    string_dialogue = '''Generate phone conversations with the following description:

    A phone conversation between a caller trying to sales insurance for the receiver and a receiver who is a scam baiter trying to proof whether the caller is a scammer or not. The receiver should realize that the caller isn't a scammer after few replies.
    Do not put any description other than the conversation. Do not put action description such as (pauses) in the conversation. 
    
    Format the response as follows: 
    caller: [dialogue] 
    receiver: [dialogue]
    '''

    input = {
        "prompt": string_dialogue,
        "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "temperature":temperature, 
        "top_p":top_p, 
        "max_new_tokens":max_length, 
        "repetition_penalty":1
    }

    output = replicate.run(llm, input=input)

    return output

# response = generate_llama_response()
# full_response = ''
# for item in response:
#     full_response += item
# print(full_response)

insurance_nonscam_data = pd.DataFrame(columns=['dialogue', 'type', 'label'])

# Generate multiple responses and add them to the DataFrame
num_responses = 150
for i in range(num_responses):
    response = generate_llama_response()
    full_response = ''
    for item in response:
        full_response += item
    print(f"Response {i+1}:")
    print(full_response)
    insurance_nonscam_data = insurance_nonscam_data._append({'dialogue': full_response, 'type': 'insurance', 'label': 0}, ignore_index=True)

# Function to format the cell value
def format_cell(cell):
    return ' '.join(str(cell).split('\n'))

# Apply the formatting function to each cell in the DataFrame
insurance_nonscam_data = insurance_nonscam_data.map(format_cell) 

# Save the DataFrame to a CSV file
insurance_nonscam_data.to_csv('insurance_nonscam_responses_150.csv', index=False)