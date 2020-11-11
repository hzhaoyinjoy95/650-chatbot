from flask import Flask, render_template, request
import math 
import metapy
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    what_the_user_said = request.args.get('msg')

    # TODO: Design a ranking function that treats what_the_user_said as the
    # query and returns the set of relevant responses to that. Your bot can
    # respond with any relevant response or the most-relevant.
    # See the homework for suggestions on possible rankers.

    return "I don't know"

if __name__ == "__main__":

    
    # IMPLEMENTATION HINT: you probably want to load and cache your conversation
    # database (provided by us) here before the chatbot runs
       
    app.run()
