from flask import Flask, jsonify
from flask import request
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv()
from src.model.model import chat_session
 

app = Flask(__name__)

@app.route("/")
def main():
   return jsonify({"Message": "Working and alive", "Code":200 })

@app.route('/help')
def index():
   symptom = request.args.get("symptom") 
   if symptom == None:
      return jsonify({"Error":"Please pass a symptom", "Code": 400})
   else:
       response = chat_session.send_message(symptom)
       return jsonify({"Response": response.text, "Code": 200})
   



if __name__ == '__main__':
   app.run()