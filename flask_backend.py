from flask import Flask
from flask import Flask,render_template,request
from numpy.core.records import fromrecords
from main import start
import datetime 
import json 

frequency = { } 
def init_freq(): 
     for i in range(24): 
         frequency[i] = 0; 



init_freq()


app = Flask(__name__)

@app.route("/")
def index(): 
    now = datetime.datetime.now()
    # print(now.hour, now.minute)
    if now.hour == 0 and now.minute ==0: 
        frequency.clear()
        init_freq()
    if now.hour in frequency: 

        frequency[now.hour] += 1 
    else: 

        frequency[now.hour ] = 0 
    
    # print(frequency)
    return render_template("index.html") 

@app.route("/get")
def chat_bot(): 
    user_input = request.args.get("user-input")
    print(user_input)

   
    if request.method == "GET" and user_input != None:
        print('request_received')
        bot_response = start(user_input)
        print(bot_response)
        return bot_response 
    return "test_response"

@app.route("/frequency")
def freq(): 
   
    json_object = json.dumps(frequency, indent = 4)  
    return json_object 
if __name__ == "__main__": 
    app.run(debug=True)