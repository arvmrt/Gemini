import os
import google.generativeai as genai

# Define your prompt with question
prompt = "Who is the first president of USA?"

'''
Setup a environment variable on Linux Server with name GOOGLE_API_KEY and save the key in there. Make sure to run source command to enable the variable.
# vi .bashrc
export GOOGLE_API_KEY="<Input your API Key Here>"  #Add this line at end of file and save file.
# source .bashrc
'''
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Create the Model
model = genai.GenerativeModel('gemini-pro')

# Send the prompt to model and capture output in "response" variable
response = model.generate_content(prompt)    

# Print the ooutput value
print(response.text)
