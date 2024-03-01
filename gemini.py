import os
import google.generativeai as genai

# Define your prompt with question
prompt = "Hi there! Thanks for using Gemini-pro"

# Add your API Key
genai.configure(os.environ.get("GENAI_API_KEY"))

# Create the Model
model = genai.GenerativeModel('gemini-pro')

# Send the prompt to model and capture output in "response" variable
response = model.generate_content(prompt)    

# Print the ooutput value
print(response.text)
