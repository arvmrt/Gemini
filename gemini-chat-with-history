import os
import google.generativeai as genai

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

# Create a variable containing previous chat history. Note below format is must else it will give error.
chat_history = [
   {
      'role': 'user',
      'parts': ['Who is the first president of USA']
   },
   {
      'role': 'model',
      'parts': ['George Washington']
   }
]

# Initialize the chat
chat = model.start_chat(history=chat_history)

# Now ask a question with context of the previouly given history 
response = chat.send_message("and who is 16th ?")
print(response.text)
