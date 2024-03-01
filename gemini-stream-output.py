import os
import google.generativeai as genai

# Define your prompt with question
prompt = "Hi there! Thanks for using Gemini-pro"

# Add your API Key. Make sure you setup a environment variable with name "GENAI_API_KEY" containing your API Key.
genai.configure(os.environ.get("GENAI_API_KEY"))

# Create the Model
model = genai.GenerativeModel('gemini-pro', stream=True)

# Send the prompt to model and capture output in "response" variable
response = model.generate_content(prompt)    

for chunk in response:
  print(chunk.text)
  print("_"*80)
