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

# Initialize the chat
chat = model.start_chat(history=[])

# Create a loop for contineous chat with Gemini and break when user type "quit"
while True:
    user_prompt = input("\nYou: ")
    if user_prompt == "quit":
        break
        
    response = chat.send_message(user_prompt)
    print("Gemani: " + str(response.text))
