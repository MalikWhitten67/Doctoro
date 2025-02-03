import os
import google.generativeai as genai 
genai.configure(api_key=os.getenv("api_key"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
data = ""
with open(os.getcwd() + "./src/Models/001/index.txt", "r") as file:
    data = file.read();
    file.close()
    pass


model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction=data,
)

chat_session = model.start_chat(
  history=[
  ]
)  


