from flask import Flask
from flask import Flask,render_template,request
from main import start 



app = Flask(__name__)

@app.route("/")
def index(): 
    bot_response = chat_bot()
    return render_template("index.html", bot_response=bot_response) 

@app.route("/get")
def chat_bot(): 
    user_input = request.args.get("user-input")
    print(user_input)
    if request.method == "GET" and user_input != None:
        print('request_received')
        # print(user_input)
        bot_response = start(user_input)
        print(bot_response)
        return bot_response 
    return "test_response"

if __name__ == "__main__": 
    app.run(debug=True)